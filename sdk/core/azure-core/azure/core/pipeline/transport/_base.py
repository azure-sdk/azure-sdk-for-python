# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from __future__ import annotations
import abc
from email.message import Message
import json
import logging
import time
import copy
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

from typing import (
    Generic,
    TypeVar,
    IO,
    Union,
    Any,
    Mapping,
    Optional,
    Tuple,
    Iterator,
    Type,
    Dict,
    List,
    Sequence,
    MutableMapping,
    ContextManager,
    TYPE_CHECKING,
)

from http.client import HTTPResponse as _HTTPResponse

from azure.core.exceptions import HttpResponseError
from azure.core.pipeline.policies import SansIOHTTPPolicy
from ...utils._utils import case_insensitive_dict
from ...utils._pipeline_transport_rest_shared import (
    _format_parameters_helper,
    _prepare_multipart_body_helper,
    _serialize_request,
    _format_data_helper,
    BytesIOSocket,
    _decode_parts_helper,
    _get_raw_parts_helper,
    _parts_helper,
)


HTTPResponseType = TypeVar("HTTPResponseType")
HTTPRequestType = TypeVar("HTTPRequestType")
DataType = Union[bytes, str, Dict[str, Union[str, int]]]

if TYPE_CHECKING:
    # We need a transport to define a pipeline, this "if" avoid a circular import
    from azure.core.pipeline import Pipeline
    from azure.core.rest._helpers import FileContent

_LOGGER = logging.getLogger(__name__)

binary_type = str


def _format_url_section(template, **kwargs: Dict[str, str]) -> str:
    """String format the template with the kwargs, auto-skip sections of the template that are NOT in the kwargs.

    By default in Python, "format" will raise a KeyError if a template element is not found. Here the section between
    the slashes will be removed from the template instead.

    This is used for API like Storage, where when Swagger has template section not defined as parameter.

    :param str template: a string template to fill
    :rtype: str
    :returns: Template completed
    """
    last_template = template
    components = template.split("/")
    while components:
        try:
            return template.format(**kwargs)
        except KeyError as key:
            formatted_components = template.split("/")
            components = [c for c in formatted_components if "{{{}}}".format(key.args[0]) not in c]
            template = "/".join(components)
            if last_template == template:
                raise ValueError(
                    f"The value provided for the url part '{template}' was incorrect, and resulted in an invalid url"
                ) from key
            last_template = template
    return last_template


def _urljoin(base_url: str, stub_url: str) -> str:
    """Append to end of base URL without losing query parameters.

    :param str base_url: The base URL.
    :param str stub_url: Section to append to the end of the URL path.
    :returns: The updated URL.
    :rtype: str
    """
    parsed_base_url = urlparse(base_url)

    # Can't use "urlparse" on a partial url, we get incorrect parsing for things like
    # document:build?format=html&api-version=2019-05-01
    split_url = stub_url.split("?", 1)
    stub_url_path = split_url.pop(0)
    stub_url_query = split_url.pop() if split_url else None

    # Note that _replace is a public API named that way to avoid conflicts in namedtuple
    # https://docs.python.org/3/library/collections.html?highlight=namedtuple#collections.namedtuple
    parsed_base_url = parsed_base_url._replace(
        path=parsed_base_url.path.rstrip("/") + "/" + stub_url_path,
    )
    if stub_url_query:
        query_params = [stub_url_query]
        if parsed_base_url.query:
            query_params.insert(0, parsed_base_url.query)
        parsed_base_url = parsed_base_url._replace(query="&".join(query_params))
    return parsed_base_url.geturl()


class HttpTransport(ContextManager["HttpTransport"], abc.ABC, Generic[HTTPRequestType, HTTPResponseType]):
    """An http sender ABC."""

    @abc.abstractmethod
    def send(self, request: HTTPRequestType, **kwargs: Any) -> HTTPResponseType:
        """Send the request using this HTTP sender.

        :param request: The pipeline request object
        :type request: ~azure.core.transport.HTTPRequest
        :return: The pipeline response object.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """

    @abc.abstractmethod
    def open(self) -> None:
        """Assign new session if one does not already exist."""

    @abc.abstractmethod
    def close(self) -> None:
        """Close the session if it is not externally owned."""

    def sleep(self, duration: float) -> None:
        """Sleep for the specified duration.

        You should always ask the transport to sleep, and not call directly
        the stdlib. This is mostly important in async, as the transport
        may not use asyncio but other implementations like trio and they have their own
        way to sleep, but to keep design
        consistent, it's cleaner to always ask the transport to sleep and let the transport
        implementor decide how to do it.

        :param float duration: The number of seconds to sleep.
        """
        time.sleep(duration)


class HttpRequest:
    """Represents an HTTP request.

    URL can be given without query parameters, to be added later using "format_parameters".

    :param str method: HTTP method (GET, HEAD, etc.)
    :param str url: At least complete scheme/host/path
    :param dict[str,str] headers: HTTP headers
    :param files: Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart
        encoding upload. ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple
        ``('filename', fileobj, 'content_type')`` or a 4-tuple
        ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
        defining the content type of the given file and ``custom_headers``
        a dict-like object containing additional headers to add for the file.
    :type files: dict[str, tuple[str, IO, str, dict]] or dict[str, IO]
    :param data: Body to be sent.
    :type data: bytes or dict (for form)
    """

    def __init__(
        self,
        method: str,
        url: str,
        headers: Optional[Mapping[str, str]] = None,
        files: Optional[Any] = None,
        data: Optional[DataType] = None,
    ) -> None:
        self.method = method
        self.url = url
        self.headers: MutableMapping[str, str] = case_insensitive_dict(headers)
        self.files: Optional[Any] = files
        self.data: Optional[DataType] = data
        self.multipart_mixed_info: Optional[Tuple[Sequence[Any], Sequence[Any], Optional[str], Dict[str, Any]]] = None

    def __repr__(self) -> str:
        return "<HttpRequest [{}], url: '{}'>".format(self.method, self.url)

    def __deepcopy__(self, memo: Optional[Dict[int, Any]] = None) -> "HttpRequest":
        try:
            data = copy.deepcopy(self.body, memo)
            files = copy.deepcopy(self.files, memo)
            request = HttpRequest(self.method, self.url, self.headers, files, data)
            request.multipart_mixed_info = self.multipart_mixed_info
            return request
        except (ValueError, TypeError):
            return copy.copy(self)

    @property
    def query(self) -> Dict[str, str]:
        """The query parameters of the request as a dict.

        :rtype: dict[str, str]
        :return: The query parameters of the request as a dict.
        """
        query = urlparse(self.url).query
        if query:
            return {p[0]: p[-1] for p in [p.partition("=") for p in query.split("&")]}
        return {}

    @property
    def body(self) -> Optional[DataType]:
        """Alias to data.

        :rtype: bytes or str or dict or None
        :return: The body of the request.
        """
        return self.data

    @body.setter
    def body(self, value: Optional[DataType]) -> None:
        self.data = value

    @staticmethod
    def _format_data(data: Union[str, IO]) -> Union[Tuple[Optional[str], str], Tuple[Optional[str], FileContent, str]]:
        """Format field data according to whether it is a stream or
        a string for a form-data request.

        :param data: The request field data.
        :type data: str or file-like object.
        :rtype: tuple[str, IO, str] or tuple[None, str]
        :return: A tuple of (data name, data IO, "application/octet-stream") or (None, data str)
        """
        return _format_data_helper(data)

    def format_parameters(self, params: Dict[str, str]) -> None:
        """Format parameters into a valid query string.
        It's assumed all parameters have already been quoted as
        valid URL strings.

        :param dict params: A dictionary of parameters.
        """
        return _format_parameters_helper(self, params)

    def set_streamed_data_body(self, data: Any) -> None:
        """Set a streamable data body.

        :param data: The request field data.
        :type data: stream or generator or asyncgenerator
        """
        if not isinstance(data, binary_type) and not any(
            hasattr(data, attr) for attr in ["read", "__iter__", "__aiter__"]
        ):
            raise TypeError("A streamable data source must be an open file-like object or iterable.")
        self.data = data
        self.files = None

    def set_text_body(self, data: str) -> None:
        """Set a text as body of the request.

        :param data: A text to send as body.
        :type data: str
        """
        if data is None:
            self.data = None
        else:
            self.data = data
            self.headers["Content-Length"] = str(len(self.data))
        self.files = None

    def set_xml_body(self, data: Any) -> None:
        """Set an XML element tree as the body of the request.

        :param data: The request field data.
        :type data: XML node
        """
        if data is None:
            self.data = None
        else:
            bytes_data: bytes = ET.tostring(data, encoding="utf8")
            self.data = bytes_data.replace(b"encoding='utf8'", b"encoding='utf-8'")
            self.headers["Content-Length"] = str(len(self.data))
        self.files = None

    def set_json_body(self, data: Any) -> None:
        """Set a JSON-friendly object as the body of the request.

        :param data: A JSON serializable object
        :type data: dict
        """
        if data is None:
            self.data = None
        else:
            self.data = json.dumps(data)
            self.headers["Content-Length"] = str(len(self.data))
        self.files = None

    def set_formdata_body(self, data: Optional[Dict[str, str]] = None) -> None:
        """Set form-encoded data as the body of the request.

        :param data: The request field data.
        :type data: dict
        """
        if data is None:
            data = {}
        content_type = self.headers.pop("Content-Type", None) if self.headers else None

        if content_type and content_type.lower() == "application/x-www-form-urlencoded":
            self.data = {f: d for f, d in data.items() if d is not None}
            self.files = None
        else:  # Assume "multipart/form-data"
            self.files = {f: self._format_data(d) for f, d in data.items() if d is not None}
            self.data = None

    def set_bytes_body(self, data: bytes) -> None:
        """Set generic bytes as the body of the request.

        Will set content-length.

        :param data: The request field data.
        :type data: bytes
        """
        if data:
            self.headers["Content-Length"] = str(len(data))
        self.data = data
        self.files = None

    def set_multipart_mixed(
        self,
        *requests: "HttpRequest",
        policies: Optional[List[SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]]] = None,
        boundary: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Set the part of a multipart/mixed.

        Only supported args for now are HttpRequest objects.

        boundary is optional, and one will be generated if you don't provide one.
        Note that no verification are made on the boundary, this is considered advanced
        enough so you know how to respect RFC1341 7.2.1 and provide a correct boundary.

        Any additional kwargs will be passed into the pipeline context for per-request policy
        configuration.

        :param requests: The requests to add to the multipart/mixed
        :type requests: ~azure.core.pipeline.transport.HttpRequest
        :keyword list[SansIOHTTPPolicy] policies: SansIOPolicy to apply at preparation time
        :keyword str boundary: Optional boundary
        """
        policies = policies or []
        self.multipart_mixed_info = (
            requests,
            policies,
            boundary,
            kwargs,
        )

    def prepare_multipart_body(self, content_index: int = 0) -> int:
        """Will prepare the body of this request according to the multipart information.

        This call assumes the on_request policies have been applied already in their
        correct context (sync/async)

        Does nothing if "set_multipart_mixed" was never called.

        :param int content_index: The current index of parts within the batch message.
        :returns: The updated index after all parts in this request have been added.
        :rtype: int
        """
        return _prepare_multipart_body_helper(self, content_index)

    def serialize(self) -> bytes:
        """Serialize this request using application/http spec.

        :rtype: bytes
        :return: The requests serialized as HTTP low-level message in bytes.
        """
        return _serialize_request(self)


class _HttpResponseBase:
    """Represent a HTTP response.

    No body is defined here on purpose, since async pipeline
    will provide async ways to access the body
    Full in-memory using "body" as bytes.

    :param request: The request.
    :type request: ~azure.core.pipeline.transport.HttpRequest
    :param internal_response: The object returned from the HTTP library.
    :type internal_response: any
    :param int block_size: Defaults to 4096 bytes.
    """

    def __init__(
        self,
        request: "HttpRequest",
        internal_response: Any,
        block_size: Optional[int] = None,
    ) -> None:
        self.request: HttpRequest = request
        self.internal_response = internal_response
        # This is actually never None, and set by all implementations after the call to
        # __init__ of this class. This class is also a legacy impl, so it's risky to change it
        # for low benefits The new "rest" implementation does define correctly status_code
        # as non-optional.
        self.status_code: int = None  # type: ignore
        self.headers: MutableMapping[str, str] = {}
        self.reason: Optional[str] = None
        self.content_type: Optional[str] = None
        self.block_size: int = block_size or 4096  # Default to same as Requests

    def body(self) -> bytes:
        """Return the whole body as bytes in memory.

        Sync implementer should load the body in memory if they can.
        Async implementer should rely on async load_body to have been called first.

        :rtype: bytes
        :return: The whole body as bytes in memory.
        """
        raise NotImplementedError()

    def text(self, encoding: Optional[str] = None) -> str:
        """Return the whole body as a string.

        .. seealso:: ~body()

        :param str encoding: The encoding to apply. If None, use "utf-8" with BOM parsing (utf-8-sig).
         Implementation can be smarter if they want (using headers or chardet).
        :rtype: str
        :return: The whole body as a string.
        """
        if encoding == "utf-8" or encoding is None:
            encoding = "utf-8-sig"
        return self.body().decode(encoding)

    def _decode_parts(
        self,
        message: Message,
        http_response_type: Type["_HttpResponseBase"],
        requests: Sequence[HttpRequest],
    ) -> List["HttpResponse"]:
        """Rebuild an HTTP response from pure string.

        :param ~email.message.Message message: The HTTP message as an email object
        :param type http_response_type: The type of response to return
        :param list[HttpRequest] requests: The requests that were batched together
        :rtype: list[HttpResponse]
        :return: The list of HttpResponse
        """
        return _decode_parts_helper(self, message, http_response_type, requests, _deserialize_response)

    def _get_raw_parts(
        self, http_response_type: Optional[Type["_HttpResponseBase"]] = None
    ) -> Iterator["HttpResponse"]:
        """Assuming this body is multipart, return the iterator or parts.

        If parts are application/http use http_response_type or HttpClientTransportResponse
        as envelope.

        :param type http_response_type: The type of response to return
        :rtype: iterator[HttpResponse]
        :return: The iterator of HttpResponse
        """
        return _get_raw_parts_helper(self, http_response_type or HttpClientTransportResponse)

    def raise_for_status(self) -> None:
        """Raises an HttpResponseError if the response has an error status code.
        If response is good, does nothing.
        """
        if not self.status_code or self.status_code >= 400:
            raise HttpResponseError(response=self)

    def __repr__(self) -> str:
        content_type_str = ", Content-Type: {}".format(self.content_type) if self.content_type else ""
        return "<{}: {} {}{}>".format(type(self).__name__, self.status_code, self.reason, content_type_str)


class HttpResponse(_HttpResponseBase):
    """Represent a HTTP response."""

    def stream_download(self, pipeline: Pipeline[HttpRequest, "HttpResponse"], **kwargs: Any) -> Iterator[bytes]:
        """Generator for streaming request body data.

        Should be implemented by sub-classes if streaming download
        is supported.

        :param pipeline: The pipeline object
        :type pipeline: ~azure.core.pipeline.Pipeline
        :rtype: iterator[bytes]
        :return: The generator of bytes connected to the socket
        """
        raise NotImplementedError("stream_download is not implemented.")

    def parts(self) -> Iterator["HttpResponse"]:
        """Assuming the content-type is multipart/mixed, will return the parts as an iterator.

        :rtype: iterator[HttpResponse]
        :return: The iterator of HttpResponse if request was multipart/mixed
        :raises ValueError: If the content is not multipart/mixed
        """
        return _parts_helper(self)


class _HttpClientTransportResponse(_HttpResponseBase):
    """Create a HTTPResponse from an http.client response.

    Body will NOT be read by the constructor. Call "body()" to load the body in memory if necessary.

    :param HttpRequest request: The request.
    :param httpclient_response: The object returned from an HTTP(S)Connection from http.client
    :type httpclient_response: http.client.HTTPResponse
    """

    def __init__(self, request, httpclient_response):
        super(_HttpClientTransportResponse, self).__init__(request, httpclient_response)
        self.status_code = httpclient_response.status
        self.headers = case_insensitive_dict(httpclient_response.getheaders())
        self.reason = httpclient_response.reason
        self.content_type = self.headers.get("Content-Type")
        self.data = None

    def body(self):
        if self.data is None:
            self.data = self.internal_response.read()
        return self.data


class HttpClientTransportResponse(_HttpClientTransportResponse, HttpResponse):  # pylint: disable=abstract-method
    """Create a HTTPResponse from an http.client response.

    Body will NOT be read by the constructor. Call "body()" to load the body in memory if necessary.
    """


def _deserialize_response(http_response_as_bytes, http_request, http_response_type=HttpClientTransportResponse):
    """Deserialize a HTTPResponse from a string.

    :param bytes http_response_as_bytes: The HTTP response as bytes.
    :param HttpRequest http_request: The request to store in the response.
    :param type http_response_type: The type of response to return
    :rtype: HttpResponse
    :return: The HTTP response from those low-level bytes.
    """
    local_socket = BytesIOSocket(http_response_as_bytes)
    response = _HTTPResponse(local_socket, method=http_request.method)
    response.begin()
    return http_response_type(http_request, response)


class PipelineClientBase:
    """Base class for pipeline clients.

    :param str base_url: URL for the request.
    """

    def __init__(self, base_url: str):
        self._base_url = base_url

    def _request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, str]],
        headers: Optional[Dict[str, str]],
        content: Any,
        form_content: Optional[Dict[str, Any]],
        stream_content: Any,
    ) -> HttpRequest:
        """Create HttpRequest object.

        If content is not None, guesses will be used to set the right body:
        - If content is an XML tree, will serialize as XML
        - If content-type starts by "text/", set the content as text
        - Else, try JSON serialization

        :param str method: HTTP method (GET, HEAD, etc.)
        :param str url: URL for the request.
        :param dict params: URL query parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = HttpRequest(method, self.format_url(url))

        if params:
            request.format_parameters(params)

        if headers:
            request.headers.update(headers)

        if content is not None:
            content_type = request.headers.get("Content-Type")
            if isinstance(content, ET.Element):
                request.set_xml_body(content)
            # https://github.com/Azure/azure-sdk-for-python/issues/12137
            # A string is valid JSON, make the difference between text
            # and a plain JSON string.
            # Content-Type is a good indicator of intent from user
            elif content_type and content_type.startswith("text/"):
                request.set_text_body(content)
            else:
                try:
                    request.set_json_body(content)
                except TypeError:
                    request.data = content

        if form_content:
            request.set_formdata_body(form_content)
        elif stream_content:
            request.set_streamed_data_body(stream_content)

        return request

    def format_url(self, url_template: str, **kwargs: Any) -> str:
        """Format request URL with the client base URL, unless the
        supplied URL is already absolute.

        Note that both the base url and the template url can contain query parameters.

        :param str url_template: The request URL to be formatted if necessary.
        :rtype: str
        :return: The formatted URL.
        """
        url = _format_url_section(url_template, **kwargs)
        if url:
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                url = url.lstrip("/")
                try:
                    base = self._base_url.format(**kwargs).rstrip("/")
                except KeyError as key:
                    err_msg = "The value provided for the url part {} was incorrect, and resulted in an invalid url"
                    raise ValueError(err_msg.format(key.args[0])) from key

                url = _urljoin(base, url)
        else:
            url = self._base_url.format(**kwargs)
        return url

    def get(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        content: Any = None,
        form_content: Optional[Dict[str, Any]] = None,
    ) -> "HttpRequest":
        """Create a GET request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("GET", url, params, headers, content, form_content, None)
        request.method = "GET"
        return request

    def put(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        content: Any = None,
        form_content: Optional[Dict[str, Any]] = None,
        stream_content: Any = None,
    ) -> HttpRequest:
        """Create a PUT request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("PUT", url, params, headers, content, form_content, stream_content)
        return request

    def post(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        content: Any = None,
        form_content: Optional[Dict[str, Any]] = None,
        stream_content: Any = None,
    ) -> HttpRequest:
        """Create a POST request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("POST", url, params, headers, content, form_content, stream_content)
        return request

    def head(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        content: Any = None,
        form_content: Optional[Dict[str, Any]] = None,
        stream_content: Any = None,
    ) -> HttpRequest:
        """Create a HEAD request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("HEAD", url, params, headers, content, form_content, stream_content)
        return request

    def patch(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        content: Any = None,
        form_content: Optional[Dict[str, Any]] = None,
        stream_content: Any = None,
    ) -> HttpRequest:
        """Create a PATCH request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("PATCH", url, params, headers, content, form_content, stream_content)
        return request

    def delete(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        content: Any = None,
        form_content: Optional[Dict[str, Any]] = None,
    ) -> HttpRequest:
        """Create a DELETE request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("DELETE", url, params, headers, content, form_content, None)
        return request

    def merge(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        content: Any = None,
        form_content: Optional[Dict[str, Any]] = None,
    ) -> HttpRequest:
        """Create a MERGE request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("MERGE", url, params, headers, content, form_content, None)
        return request

    def options(
        self,  # pylint: disable=unused-argument
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        *,
        content: Optional[Union[bytes, str, Dict[Any, Any]]] = None,
        form_content: Optional[Dict[Any, Any]] = None,
        **kwargs: Any,
    ) -> HttpRequest:
        """Create a OPTIONS request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :keyword content: The body content
        :type content: bytes or str or dict
        :keyword dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
        request = self._request("OPTIONS", url, params, headers, content, form_content, None)
        return request
