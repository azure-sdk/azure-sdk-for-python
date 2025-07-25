# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import asyncio
import copy
import json
import time
import uuid
from typing import Any, Dict, List, Optional, cast, Union

from azure.ai.evaluation._http_utils import AsyncHttpPipeline, get_async_http_client
from azure.ai.evaluation._user_agent import UserAgentSingleton
from azure.core.exceptions import HttpResponseError, ServiceResponseError
from azure.core.pipeline.policies import AsyncRetryPolicy, RetryMode
from azure.ai.evaluation._common.onedp._client import AIProjectClient
from azure.ai.evaluation._common.onedp.models import SimulationDTO
from azure.ai.evaluation._common.constants import RAIService

from .._model_tools._template_handler import TemplateParameters
from .models import OpenAIChatCompletionsModel


class SimulationRequestDTO:
    """Simulation Request Data Transfer Object

    :param url: The URL to send the request to.
    :type url: str
    :param headers: The headers to send with the request.
    :type headers: Dict[str, str]
    :param payload: The payload to send with the request.
    :type payload: Dict[str, Any]
    :param params: The parameters to send with the request.
    :type params: Dict[str, str]
    :param template_key: The template key to use for the request.
    :type template_key: str
    :param template_parameters: The template parameters to use for the request.
    :type template_parameters: Dict
    """

    def __init__(
        self,
        url: str,
        headers: Dict[str, str],
        payload: Dict[str, Any],
        params: Dict[str, str],
        templateKey: str,
        templateParameters: Optional[TemplateParameters],
    ):
        self.url = url
        self.headers = headers
        self.json = json.dumps(payload)
        self.params = params
        self.templateKey = templateKey
        self.templateParameters = templateParameters

    def to_dict(self) -> Dict:
        """Convert the DTO to a dictionary.

        :return: The DTO as a dictionary.
        :rtype: Dict
        """
        toReturn = self.__dict__.copy()

        if toReturn["templateParameters"] is not None:
            toReturn["templateParameters"] = {str(k): str(v) for k, v in toReturn["templateParameters"].items()}

        return toReturn

    def to_json(self):
        """Convert the DTO to a JSON string.

        :return: The DTO as a JSON string.
        :rtype: str
        """
        return json.dumps(self.__dict__)


class ProxyChatCompletionsModel(OpenAIChatCompletionsModel):
    """A chat completion model that uses a proxy to query the model with a body of data.

    :param name: The name of the model.
    :type name: str
    :param template_key: The template key to use for the request.
    :type template_key: str
    :param template_parameters: The template parameters to use for the request.
    :type template_parameters: Dict
    :keyword args: Additional arguments to pass to the parent class.
    :keyword kwargs: Additional keyword arguments to pass to the parent class.
    """

    def __init__(self, name: str, template_key: str, template_parameters: TemplateParameters, **kwargs) -> None:
        self.tkey = template_key
        self.tparam = template_parameters
        self.result_url: Optional[str] = None
        self.simulation_id: Optional[str] = kwargs.pop("simulation_id", "")

        super().__init__(name=name, **kwargs)

    def format_request_data(self, messages: List[Dict], **request_params) -> Dict:  # type: ignore[override]
        """Format the request data to query the model with.

        :param messages: List of messages to query the model with.
            Expected format: [{"role": "user", "content": "Hello!"}, ...]
        :type messages: List[Dict]
        :keyword request_params: Additional parameters to pass to the model.
        :paramtype request_params: Dict
        :return: The formatted request data.
        :rtype: Dict
        """
        request_data = {"messages": messages, **self.get_model_params()}
        request_data.update(request_params)
        return request_data

    async def get_conversation_completion(
        self,
        messages: List[Dict],
        session: Union[AsyncHttpPipeline, AIProjectClient],
        role: str = "assistant",  # pylint: disable=unused-argument
        **request_params,
    ) -> dict:
        """
        Query the model a single time with a message.

        :param messages: List of messages to query the model with.
            Expected format: [{"role": "user", "content": "Hello!"}, ...]
        :type messages: List[Dict]
        :param session: AsyncHttpPipeline object to query the model with.
        :type session: ~azure.ai.evaluation._http_utils.AsyncHttpPipeline
        :param role: The role of the user sending the message. This parameter is not used in this method;
            however, it must be included to match the method signature of the parent class. Defaults to "assistant".
        :type role: str
        :keyword request_params: Additional parameters to pass to the model.
        :paramtype request_params: Dict
        :return: A dictionary representing the completion of the conversation query.
        :rtype: Dict
        """
        request_data = self.format_request_data(
            messages=messages,
            **request_params,
        )
        return await self.request_api(
            session=session,
            request_data=request_data,
        )

    async def request_api(
        self,
        session: Union[AsyncHttpPipeline, AIProjectClient],
        request_data: dict,
    ) -> dict:
        """
        Request the model with a body of data.

        :param session: HTTPS Session for invoking the endpoint.
        :type session: AsyncHttpPipeline
        :param request_data: Prompt dictionary to query the model with. (Pass {"prompt": prompt} instead of prompt.)
        :type request_data: Dict[str, Any]
        :return: A body of data resulting from the model query.
        :rtype: Dict[str, Any]
        """

        self._log_request(request_data)

        token = self.token_manager.get_token()

        proxy_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": UserAgentSingleton().value,
        }

        headers = {
            "Content-Type": "application/json",
            "X-CV": f"{uuid.uuid4()}",
            "X-ModelType": self.model or "",
            "x-ms-client-request-id": self.simulation_id,
        }
        # add all additional headers
        headers.update(self.additional_headers)  # type: ignore[arg-type]
        params = {}
        if self.api_version:
            params["api-version"] = self.api_version

        sim_request_dto = SimulationRequestDTO(
            url=self.endpoint_url,
            headers=headers,
            payload=request_data,
            params=params,
            templateKey=self.tkey,
            templateParameters=self.tparam,
        )

        time_start = time.time()
        full_response = None

        if isinstance(session, AIProjectClient):
            sim_request_dto = SimulationDTO(
                headers=headers,
                params=params,
                json=json.dumps(request_data),
                template_key=self.tkey,
                template_parameters=self.tparam,
            )
            response_data = session.red_teams.submit_simulation(sim_request_dto, headers=headers, params=params)
            operation_id = response_data["location"].split("/")[-1]

            request_count = 0
            flag = True
            while flag:
                try:
                    response = session.evaluations.operation_results(operation_id, headers=headers)
                except Exception as e:
                    from types import SimpleNamespace  # pylint: disable=forgotten-debug-statement

                    response = SimpleNamespace(status_code=202, text=str(e), json=lambda: {"error": str(e)})
                if isinstance(response, dict):
                    response_data = response
                    flag = False
                    break
                if response.status_code == 200:
                    response_data = cast(List[Dict], response.json())
                    flag = False
                else:
                    request_count += 1
                    sleep_time = RAIService.SLEEP_TIME**request_count
                    await asyncio.sleep(sleep_time)
        else:
            # Retry policy for POST request to RAI service
            service_call_retry_policy = AsyncRetryPolicy(
                retry_on_exceptions=[ServiceResponseError],
                retry_total=7,
                retry_backoff_factor=10.0,
                retry_backoff_max=180,
                retry_mode=RetryMode.Exponential,
            )

            response = None
            async with get_async_http_client().with_policies(retry_policy=service_call_retry_policy) as retry_client:
                try:
                    response = await retry_client.post(
                        url=self.endpoint_url, headers=proxy_headers, json=sim_request_dto.to_dict()
                    )
                except ServiceResponseError as e:
                    self.logger.error("ServiceResponseError during POST request to rai svc after retries: %s", str(e))
                    raise

            # response.raise_for_status()
            if response.status_code != 202:
                raise HttpResponseError(
                    message=f"Received unexpected HTTP status: {response.status_code} {response.text()}",
                    response=response,
                )
            response_data = response.json()

            self.result_url = cast(str, response_data["location"])
            retry_policy = AsyncRetryPolicy(  # set up retry configuration
                retry_on_status_codes=[202],  # on which statuses to retry
                retry_total=7,
                retry_backoff_factor=10.0,
                retry_backoff_max=180,
                retry_mode=RetryMode.Exponential,
            )

            # initial 15 seconds wait before attempting to fetch result
            # Need to wait both in this thread and in the async thread for some reason?
            # Someone not under a crunch and with better async understandings should dig into this more.
            await asyncio.sleep(15)
            time.sleep(15)

            async with get_async_http_client().with_policies(retry_policy=retry_policy) as exp_retry_client:
                token = await self.token_manager.get_token_async()
                proxy_headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "User-Agent": UserAgentSingleton().value,
                }
                response = await exp_retry_client.get(  # pylint: disable=too-many-function-args,unexpected-keyword-arg
                    self.result_url, headers=proxy_headers
                )
            response.raise_for_status()
            response_data = response.json()

        self.logger.info("Response: %s", response_data)

        # Copy the full response and return it to be saved in jsonl.
        full_response = copy.copy(response_data)

        time_taken = time.time() - time_start

        # pylint: disable=unexpected-keyword-arg
        parsed_response = self._parse_response(response_data, request_data=request_data)  # type: ignore[call-arg]

        return {
            "request": request_data,
            "response": parsed_response,
            "time_taken": time_taken,
            "full_response": full_response,
        }
