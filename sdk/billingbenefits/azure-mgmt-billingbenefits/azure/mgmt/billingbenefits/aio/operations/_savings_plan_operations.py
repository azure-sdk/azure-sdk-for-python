# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._savings_plan_operations import (
    build_get_request,
    build_list_all_request,
    build_list_request,
    build_update_request,
    build_validate_update_request,
)
from .._vendor import BillingBenefitsRPMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SavingsPlanOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.billingbenefits.aio.BillingBenefitsRP`'s
        :attr:`savings_plan` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, savings_plan_order_id: str, **kwargs: Any) -> AsyncIterable["_models.SavingsPlanModel"]:
        """List savings plans in an order.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SavingsPlanModel or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.billingbenefits.models.SavingsPlanModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-11-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.SavingsPlanModelList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    savings_plan_order_id=savings_plan_order_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SavingsPlanModelList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans"}

    @distributed_trace
    def list_all(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        refresh_summary: Optional[str] = None,
        skiptoken: Optional[float] = None,
        selected_state: Optional[str] = None,
        take: Optional[float] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.SavingsPlanModel"]:
        """List savings plans.

        :param filter: May be used to filter by reservation properties. The filter supports 'eq', 'or',
         and 'and'. It does not currently support 'ne', 'gt', 'le', 'ge', or 'not'. Reservation
         properties include sku/name, properties/{appliedScopeType, archived, displayName,
         displayProvisioningState, effectiveDateTime, expiryDate, provisioningState, quantity, renew,
         reservedResourceType, term, userFriendlyAppliedScopeType, userFriendlyRenewState}. Default
         value is None.
        :type filter: str
        :param orderby: May be used to sort order by reservation properties. Default value is None.
        :type orderby: str
        :param refresh_summary: To indicate whether to refresh the roll up counts of the savings plans
         group by provisioning states. Default value is None.
        :type refresh_summary: str
        :param skiptoken: The number of savings plans to skip from the list before returning results.
         Default value is None.
        :type skiptoken: float
        :param selected_state: The selected provisioning state. Default value is None.
        :type selected_state: str
        :param take: To number of savings plans to return. Default value is None.
        :type take: float
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SavingsPlanModel or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.billingbenefits.models.SavingsPlanModel]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-11-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.SavingsPlanModelListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_all_request(
                    filter=filter,
                    orderby=orderby,
                    refresh_summary=refresh_summary,
                    skiptoken=skiptoken,
                    selected_state=selected_state,
                    take=take,
                    api_version=api_version,
                    template_url=self.list_all.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SavingsPlanModelListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_all.metadata = {"url": "/providers/Microsoft.BillingBenefits/savingsPlans"}

    @distributed_trace_async
    async def get(self, savings_plan_order_id: str, savings_plan_id: str, **kwargs: Any) -> _models.SavingsPlanModel:
        """Get savings plan.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SavingsPlanModel or the result of cls(response)
        :rtype: ~azure.mgmt.billingbenefits.models.SavingsPlanModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-11-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.SavingsPlanModel] = kwargs.pop("cls", None)

        request = build_get_request(
            savings_plan_order_id=savings_plan_order_id,
            savings_plan_id=savings_plan_id,
            expand=self._config.expand,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SavingsPlanModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}"
    }

    @overload
    async def update(
        self,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: _models.SavingsPlanUpdateRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.SavingsPlanModel]:
        """Update savings plan.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Required.
        :type body: ~azure.mgmt.billingbenefits.models.SavingsPlanUpdateRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SavingsPlanModel or None or the result of cls(response)
        :rtype: ~azure.mgmt.billingbenefits.models.SavingsPlanModel or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.SavingsPlanModel]:
        """Update savings plan.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SavingsPlanModel or None or the result of cls(response)
        :rtype: ~azure.mgmt.billingbenefits.models.SavingsPlanModel or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: Union[_models.SavingsPlanUpdateRequest, IO],
        **kwargs: Any
    ) -> Optional[_models.SavingsPlanModel]:
        """Update savings plan.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for patching a savings plan order alias. Is either a model type or a
         IO type. Required.
        :type body: ~azure.mgmt.billingbenefits.models.SavingsPlanUpdateRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SavingsPlanModel or None or the result of cls(response)
        :rtype: ~azure.mgmt.billingbenefits.models.SavingsPlanModel or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
            404: lambda response: ResourceNotFoundError(response=response, error_format=ARMErrorFormat),
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-11-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.SavingsPlanModel]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "SavingsPlanUpdateRequest")

        request = build_update_request(
            savings_plan_order_id=savings_plan_order_id,
            savings_plan_id=savings_plan_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("SavingsPlanModel", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    update.metadata = {
        "url": "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}"
    }

    @overload
    async def validate_update(
        self,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: _models.SavingsPlanUpdateValidateRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SavingsPlanValidateResponse:
        """Validate savings plan patch.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for validating a savings plan patch request. Required.
        :type body: ~azure.mgmt.billingbenefits.models.SavingsPlanUpdateValidateRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SavingsPlanValidateResponse or the result of cls(response)
        :rtype: ~azure.mgmt.billingbenefits.models.SavingsPlanValidateResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def validate_update(
        self,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SavingsPlanValidateResponse:
        """Validate savings plan patch.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for validating a savings plan patch request. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SavingsPlanValidateResponse or the result of cls(response)
        :rtype: ~azure.mgmt.billingbenefits.models.SavingsPlanValidateResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def validate_update(
        self,
        savings_plan_order_id: str,
        savings_plan_id: str,
        body: Union[_models.SavingsPlanUpdateValidateRequest, IO],
        **kwargs: Any
    ) -> _models.SavingsPlanValidateResponse:
        """Validate savings plan patch.

        :param savings_plan_order_id: Order ID of the savings plan. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: ID of the savings plan. Required.
        :type savings_plan_id: str
        :param body: Request body for validating a savings plan patch request. Is either a model type
         or a IO type. Required.
        :type body: ~azure.mgmt.billingbenefits.models.SavingsPlanUpdateValidateRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SavingsPlanValidateResponse or the result of cls(response)
        :rtype: ~azure.mgmt.billingbenefits.models.SavingsPlanValidateResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-11-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SavingsPlanValidateResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, "SavingsPlanUpdateValidateRequest")

        request = build_validate_update_request(
            savings_plan_order_id=savings_plan_order_id,
            savings_plan_id=savings_plan_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.validate_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SavingsPlanValidateResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validate_update.metadata = {
        "url": "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}/validate"
    }
