# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import AsyncPipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._utils.serialization import Deserializer, Serializer
from ...operations._service_diagnostic_settings_operations import (
    build_create_or_update_request,
    build_get_request,
    build_update_request,
)
from .._configuration import MonitorManagementClientConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ServiceDiagnosticSettingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.monitor.aio.MonitorManagementClient`'s
        :attr:`service_diagnostic_settings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: MonitorManagementClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, resource_uri: str, **kwargs: Any) -> _models.ServiceDiagnosticSettingsResource:
        """Gets the active diagnostic settings for the specified resource. **WARNING**\\ : This method
        will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))
        cls: ClsType[_models.ServiceDiagnosticSettingsResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_uri=resource_uri,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ServiceDiagnosticSettingsResource", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_uri: str,
        parameters: _models.ServiceDiagnosticSettingsResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Create or update new diagnostic settings for the specified resource. **WARNING**\\ : This
        method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, resource_uri: str, parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Create or update new diagnostic settings for the specified resource. **WARNING**\\ : This
        method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self, resource_uri: str, parameters: Union[_models.ServiceDiagnosticSettingsResource, IO[bytes]], **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Create or update new diagnostic settings for the specified resource. **WARNING**\\ : This
        method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param parameters: Parameters supplied to the operation. Is either a
         ServiceDiagnosticSettingsResource type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource or IO[bytes]
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ServiceDiagnosticSettingsResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ServiceDiagnosticSettingsResource")

        _request = build_create_or_update_request(
            resource_uri=resource_uri,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ServiceDiagnosticSettingsResource", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        resource_uri: str,
        service_diagnostic_settings_resource: _models.ServiceDiagnosticSettingsResourcePatch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the
        CreateOrUpdate method. **WARNING**\\ : This method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param service_diagnostic_settings_resource: Parameters supplied to the operation. Required.
        :type service_diagnostic_settings_resource:
         ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_uri: str,
        service_diagnostic_settings_resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the
        CreateOrUpdate method. **WARNING**\\ : This method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param service_diagnostic_settings_resource: Parameters supplied to the operation. Required.
        :type service_diagnostic_settings_resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_uri: str,
        service_diagnostic_settings_resource: Union[_models.ServiceDiagnosticSettingsResourcePatch, IO[bytes]],
        **kwargs: Any
    ) -> _models.ServiceDiagnosticSettingsResource:
        """Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the
        CreateOrUpdate method. **WARNING**\\ : This method will be deprecated in future releases.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param service_diagnostic_settings_resource: Parameters supplied to the operation. Is either a
         ServiceDiagnosticSettingsResourcePatch type or a IO[bytes] type. Required.
        :type service_diagnostic_settings_resource:
         ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResourcePatch or IO[bytes]
        :return: ServiceDiagnosticSettingsResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.models.ServiceDiagnosticSettingsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-09-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ServiceDiagnosticSettingsResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(service_diagnostic_settings_resource, (IOBase, bytes)):
            _content = service_diagnostic_settings_resource
        else:
            _json = self._serialize.body(service_diagnostic_settings_resource, "ServiceDiagnosticSettingsResourcePatch")

        _request = build_update_request(
            resource_uri=resource_uri,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ServiceDiagnosticSettingsResource", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
