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
import asyncio  # pylint: disable=do-not-import-asyncio
from collections.abc import AsyncIterator
import functools
import logging
from typing import (
    Any,
    Optional,
    AsyncIterator as AsyncIteratorType,
    Union,
    TYPE_CHECKING,
    overload,
    Type,
    MutableMapping,
)
from types import TracebackType
from urllib3.exceptions import (
    ProtocolError,
    NewConnectionError,
    ConnectTimeoutError,
)
import requests

from azure.core.exceptions import (
    ServiceRequestError,
    ServiceResponseError,
    IncompleteReadError,
    HttpResponseError,
)
from azure.core.pipeline import Pipeline
from ._base import HttpRequest
from ._base_async import (
    AsyncHttpResponse,
    _ResponseStopIteration,
    _iterate_response_content,
)
from ._requests_basic import (
    RequestsTransportResponse,
    _read_raw_stream,
    AzureErrorUnion,
)
from ._base_requests_async import RequestsAsyncTransportBase
from .._tools import is_rest as _is_rest
from .._tools_async import (
    handle_no_stream_rest_response as _handle_no_stream_rest_response,
)

if TYPE_CHECKING:
    from ...rest import (
        HttpRequest as RestHttpRequest,
        AsyncHttpResponse as RestAsyncHttpResponse,
    )

_LOGGER = logging.getLogger(__name__)


def _get_running_loop():
    return asyncio.get_running_loop()


class AsyncioRequestsTransport(RequestsAsyncTransportBase):
    """Identical implementation as the synchronous RequestsTransport wrapped in a class with
    asynchronous methods. Uses the built-in asyncio event loop.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START asyncio]
            :end-before: [END asyncio]
            :language: python
            :dedent: 4
            :caption: Asynchronous transport with asyncio.
    """

    async def __aenter__(self):
        return super(AsyncioRequestsTransport, self).__enter__()

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        return super(AsyncioRequestsTransport, self).__exit__(exc_type, exc_value, traceback)

    async def sleep(self, duration):  # pylint:disable=invalid-overridden-method
        await asyncio.sleep(duration)

    @overload  # type: ignore
    async def send(  # pylint:disable=invalid-overridden-method
        self, request: HttpRequest, *, proxies: Optional[MutableMapping[str, str]] = None, **kwargs: Any
    ) -> AsyncHttpResponse:
        """Send the request using this HTTP sender.

        :param request: The HttpRequest
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse

        :keyword MutableMapping proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """

    @overload
    async def send(  # pylint:disable=invalid-overridden-method
        self, request: "RestHttpRequest", *, proxies: Optional[MutableMapping[str, str]] = None, **kwargs: Any
    ) -> "RestAsyncHttpResponse":
        """Send a `azure.core.rest` request using this HTTP sender.

        :param request: The HttpRequest
        :type request: ~azure.core.rest.HttpRequest
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.rest.AsyncHttpResponse

        :keyword MutableMapping proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """

    async def send(  # pylint:disable=invalid-overridden-method
        self,
        request: Union[HttpRequest, "RestHttpRequest"],
        *,
        proxies: Optional[MutableMapping[str, str]] = None,
        **kwargs
    ) -> Union[AsyncHttpResponse, "RestAsyncHttpResponse"]:
        """Send the request using this HTTP sender.

        :param request: The HttpRequest
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse

        :keyword MutableMapping proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """
        self.open()
        loop = kwargs.get("loop", _get_running_loop())
        response = None
        error: Optional[AzureErrorUnion] = None
        data_to_send = await self._retrieve_request_data(request)
        try:
            response = await loop.run_in_executor(
                None,
                functools.partial(
                    self.session.request,
                    request.method,
                    request.url,
                    headers=request.headers,
                    data=data_to_send,
                    files=request.files,
                    verify=kwargs.pop("connection_verify", self.connection_config.verify),
                    timeout=kwargs.pop("connection_timeout", self.connection_config.timeout),
                    cert=kwargs.pop("connection_cert", self.connection_config.cert),
                    allow_redirects=False,
                    proxies=proxies,
                    **kwargs
                ),
            )
            response.raw.enforce_content_length = True

        except (
            NewConnectionError,
            ConnectTimeoutError,
        ) as err:
            error = ServiceRequestError(err, error=err)
        except requests.exceptions.ReadTimeout as err:
            error = ServiceResponseError(err, error=err)
        except requests.exceptions.ConnectionError as err:
            if err.args and isinstance(err.args[0], ProtocolError):
                error = ServiceResponseError(err, error=err)
            else:
                error = ServiceRequestError(err, error=err)
        except requests.exceptions.ChunkedEncodingError as err:
            msg = err.__str__()
            if "IncompleteRead" in msg:
                _LOGGER.warning("Incomplete download.")
                error = IncompleteReadError(err, error=err)
            else:
                _LOGGER.warning("Unable to stream download.")
                error = HttpResponseError(err, error=err)
        except requests.RequestException as err:
            error = ServiceRequestError(err, error=err)

        if error:
            raise error
        if _is_rest(request):
            from azure.core.rest._requests_asyncio import (
                RestAsyncioRequestsTransportResponse,
            )

            retval = RestAsyncioRequestsTransportResponse(
                request=request,
                internal_response=response,
                block_size=self.connection_config.data_block_size,
            )
            if not kwargs.get("stream"):
                await _handle_no_stream_rest_response(retval)
            return retval

        return AsyncioRequestsTransportResponse(request, response, self.connection_config.data_block_size)


class AsyncioStreamDownloadGenerator(AsyncIterator):
    """Streams the response body data.

    :param pipeline: The pipeline object
    :type pipeline: ~azure.core.pipeline.AsyncPipeline
    :param response: The response object.
    :type response: ~azure.core.pipeline.transport.AsyncHttpResponse
    :keyword bool decompress: If True which is default, will attempt to decode the body based
            on the *content-encoding* header.
    """

    def __init__(self, pipeline: Pipeline, response: AsyncHttpResponse, **kwargs) -> None:
        self.pipeline = pipeline
        self.request = response.request
        self.response = response
        self.block_size = response.block_size
        decompress = kwargs.pop("decompress", True)
        if len(kwargs) > 0:
            raise TypeError("Got an unexpected keyword argument: {}".format(list(kwargs.keys())[0]))
        internal_response = response.internal_response
        if decompress:
            self.iter_content_func = internal_response.iter_content(self.block_size)
        else:
            self.iter_content_func = _read_raw_stream(internal_response, self.block_size)
        self.content_length = int(response.headers.get("Content-Length", 0))

    def __len__(self):
        return self.content_length

    async def __anext__(self):
        loop = _get_running_loop()
        internal_response = self.response.internal_response
        try:
            chunk = await loop.run_in_executor(
                None,
                _iterate_response_content,
                self.iter_content_func,
            )
            if not chunk:
                raise _ResponseStopIteration()
            return chunk
        except _ResponseStopIteration:
            internal_response.close()
            raise StopAsyncIteration()  # pylint: disable=raise-missing-from
        except requests.exceptions.StreamConsumedError:
            raise
        except requests.exceptions.ChunkedEncodingError as err:
            msg = err.__str__()
            if "IncompleteRead" in msg:
                _LOGGER.warning("Incomplete download.")
                internal_response.close()
                raise IncompleteReadError(err, error=err) from err
            _LOGGER.warning("Unable to stream download.")
            internal_response.close()
            raise HttpResponseError(err, error=err) from err
        except Exception:
            _LOGGER.warning("Unable to stream download.")
            internal_response.close()
            raise


class AsyncioRequestsTransportResponse(AsyncHttpResponse, RequestsTransportResponse):  # type: ignore
    """Asynchronous streaming of data from the response."""

    def stream_download(self, pipeline, **kwargs) -> AsyncIteratorType[bytes]:  # type: ignore
        """Generator for streaming request body data.

        :param pipeline: The pipeline object
        :type pipeline: ~azure.core.pipeline.AsyncPipeline
        :rtype: AsyncIterator[bytes]
        :return: An async iterator of bytes chunks
        """
        return AsyncioStreamDownloadGenerator(pipeline, self, **kwargs)
