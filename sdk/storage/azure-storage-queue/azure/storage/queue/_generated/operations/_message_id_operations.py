# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MessageIdOperations(object):
    """MessageIdOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.storage.queue.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def update(
        self,
        pop_receipt,  # type: str
        visibilitytimeout,  # type: int
        timeout=None,  # type: Optional[int]
        request_id_parameter=None,  # type: Optional[str]
        queue_message=None,  # type: Optional["_models.QueueMessage"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """The Update operation was introduced with version 2011-08-18 of the Queue service API. The
        Update Message operation updates the visibility timeout of a message. You can also use this
        operation to update the contents of a message. A message must be in a format that can be
        included in an XML request with UTF-8 encoding, and the encoded message can be up to 64KB in
        size.

        :param pop_receipt: Required. Specifies the valid pop receipt value returned from an earlier
         call to the Get Messages or Update Message operation.
        :type pop_receipt: str
        :param visibilitytimeout: Optional. Specifies the new visibility timeout value, in seconds,
         relative to server time. The default value is 30 seconds. A specified value must be larger than
         or equal to 1 second, and cannot be larger than 7 days, or larger than 2 hours on REST protocol
         versions prior to version 2011-08-18. The visibility timeout of a message can be set to a value
         later than the expiry time.
        :type visibilitytimeout: int
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param queue_message: A Message object which can be stored in a Queue.
        :type queue_message: ~azure.storage.queue.models.QueueMessage
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/xml")
        accept = "application/xml"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['popreceipt'] = self._serialize.query("pop_receipt", pop_receipt, 'str')
        query_parameters['visibilitytimeout'] = self._serialize.query("visibilitytimeout", visibilitytimeout, 'int', maximum=604800, minimum=0)
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if queue_message is not None:
            body_content = self._serialize.body(queue_message, 'QueueMessage', is_xml=True)
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        response_headers['x-ms-popreceipt']=self._deserialize('str', response.headers.get('x-ms-popreceipt'))
        response_headers['x-ms-time-next-visible']=self._deserialize('rfc-1123', response.headers.get('x-ms-time-next-visible'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    update.metadata = {'url': '/{queueName}/messages/{messageid}'}  # type: ignore

    def delete(
        self,
        pop_receipt,  # type: str
        timeout=None,  # type: Optional[int]
        request_id_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """The Delete operation deletes the specified message.

        :param pop_receipt: Required. Specifies the valid pop receipt value returned from an earlier
         call to the Get Messages or Update Message operation.
        :type pop_receipt: str
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-
         service-operations>Setting Timeouts for Queue Service Operations.</a>.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/xml"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['popreceipt'] = self._serialize.query("pop_receipt", pop_receipt, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id_parameter is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {'url': '/{queueName}/messages/{messageid}'}  # type: ignore
