# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
import pytest
import json
import base64
import pathlib
from typing import List
from pydantic import BaseModel
import openai
from devtools_testutils import AzureRecordedTestCase
from conftest import (
    AZURE,
    OPENAI,
    AZURE_KEY,
    GPT_4_AZURE,
    GPT_4_OPENAI,
    configure_async,
    GA,
    PREVIEW,
    ENV_AZURE_OPENAI_SEARCH_ENDPOINT,
    ENV_AZURE_OPENAI_SEARCH_INDEX
)


@pytest.mark.live_test_only
class TestChatCompletionsAsync(AzureRecordedTestCase):

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE_KEY, GA), (AZURE_KEY, PREVIEW)]
    )
    async def test_azure_api_key(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, **kwargs)
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, **kwargs)
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_streamed_chat_completions(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "How do I bake a chocolate cake?"}
        ]

        response = await client_async.chat.completions.create(messages=messages, stream=True, stream_options={"include_usage": True}, **kwargs)

        async for completion in response:
            # API versions after 2023-05-15 send an empty first completion with RAI
            if len(completion.choices) > 0:
                assert completion.id
                assert completion.object == "chat.completion.chunk"
                assert completion.model
                assert completion.created
                for c in completion.choices:
                    assert c.index is not None
                    assert c.delta is not None
            if completion.usage:
                assert completion.usage.completion_tokens is not None
                assert completion.usage.prompt_tokens is not None
                assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_max_tokens(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, max_tokens=50, **kwargs)

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens <= 50
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_temperature(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, temperature=0.8, **kwargs)

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_top_p(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, top_p=0.1, **kwargs)

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_n(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, n=2, **kwargs)

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 2
        for idx, c in enumerate(completion.choices):
            assert c.finish_reason
            assert c.index == idx
            assert c.message.content
            assert c.message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_stop(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, stop=" ", **kwargs)

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_token_penalty(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            presence_penalty=2,
            frequency_penalty=2,
            **kwargs
        )

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_user(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            user="krista",
            **kwargs
        )

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_logit_bias(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What color is the ocean?"}
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            logit_bias={17585: -100, 14573: -100},
            **kwargs
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, GA), (AZURE, PREVIEW)])
    async def test_chat_completion_rai_annotations(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "how do I rob a bank with violence?"}
        ]

        # prompt filtered
        with pytest.raises(openai.BadRequestError) as e:
            completion = await client_async.chat.completions.create(
                messages=messages,
                **kwargs
            )
        e = e.value
        assert e.code == "content_filter"
        assert e.message is not None
        assert e.status_code == 400
        err = e.body
        assert err["code"] == "content_filter"
        assert err["param"] == "prompt"
        assert err["message"] is not None
        content_filter_result = err["innererror"]["content_filter_result"]
        assert content_filter_result["hate"]["filtered"] is False
        assert content_filter_result["hate"]["severity"] == "safe"
        assert content_filter_result["self_harm"]["filtered"] is False
        assert content_filter_result["self_harm"]["severity"] == "safe"
        assert content_filter_result["sexual"]["filtered"] is False
        assert content_filter_result["sexual"]["severity"] == "safe"
        assert content_filter_result["violence"]["filtered"] is True
        assert content_filter_result["violence"]["severity"] is not None

        # not filtered
        messages[1]["content"] = "What color is the ocean?"
        completion = await client_async.chat.completions.create(
            messages=messages,
            **kwargs
        )

        # prompt filter results
        prompt_filter_result = completion.prompt_filter_results[0]["content_filter_results"]
        assert prompt_filter_result["hate"]["filtered"] is False
        assert prompt_filter_result["hate"]["severity"] == "safe"
        assert prompt_filter_result["self_harm"]["filtered"] is False
        assert prompt_filter_result["self_harm"]["severity"] == "safe"
        assert prompt_filter_result["sexual"]["filtered"] is False
        assert prompt_filter_result["sexual"]["severity"] == "safe"
        assert prompt_filter_result["violence"]["filtered"] is False
        assert prompt_filter_result["violence"]["severity"] == "safe"

        # output content filter result
        output_filter_result = completion.choices[0].content_filter_results
        assert output_filter_result["hate"]["filtered"] is False
        assert output_filter_result["hate"]["severity"] == "safe"
        assert output_filter_result["self_harm"]["filtered"] is False
        assert output_filter_result["self_harm"]["severity"] == "safe"
        assert output_filter_result["sexual"]["filtered"] is False
        assert output_filter_result["sexual"]["severity"] == "safe"
        assert output_filter_result["violence"]["filtered"] is False
        assert output_filter_result["violence"]["severity"] == "safe"

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_functions(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "What's the weather like today in Seattle?"}
        ]

        functions=[
            {
                "name": "get_current_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit to use. Infer this from the users location.",
                        },
                    },
                    "required": ["location"],
                },
            }
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            functions=functions,
            **kwargs
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.role
        function_call =  completion.choices[0].message.function_call
        assert function_call.name == "get_current_weather"
        assert "Seattle" in function_call.arguments

        if api_type == "azure":
            prompt_filter_result = completion.prompt_filter_results[0]["content_filter_results"]
            assert prompt_filter_result["hate"]["filtered"] is False
            assert prompt_filter_result["hate"]["severity"] == "safe"
            assert prompt_filter_result["self_harm"]["filtered"] is False
            assert prompt_filter_result["self_harm"]["severity"] == "safe"
            assert prompt_filter_result["sexual"]["filtered"] is False
            assert prompt_filter_result["sexual"]["severity"] == "safe"
            assert prompt_filter_result["violence"]["filtered"] is False
            assert prompt_filter_result["violence"]["severity"] == "safe"

        messages.append(
            {
                "role": "function",
                "name": "get_current_weather",
                "content": "{\"temperature\": \"22\", \"unit\": \"celsius\", \"description\": \"Sunny\"}"
            }
        )
        function_completion = await client_async.chat.completions.create(
            messages=messages,
            functions=functions,
            **kwargs
        )
        assert function_completion
        assert "sunny" in function_completion.choices[0].message.content.lower()
        assert "22" in function_completion.choices[0].message.content
        assert function_completion.choices[0].message.role == "assistant"

        if api_type == "azure":
            # output content filter result
            output_filter_result = function_completion.choices[0].content_filter_results
            assert output_filter_result["hate"]["filtered"] is False
            assert output_filter_result["hate"]["severity"] == "safe"
            assert output_filter_result["self_harm"]["filtered"] is False
            assert output_filter_result["self_harm"]["severity"] == "safe"
            assert output_filter_result["sexual"]["filtered"] is False
            assert output_filter_result["sexual"]["severity"] == "safe"
            assert output_filter_result["violence"]["filtered"] is False
            assert output_filter_result["violence"]["severity"] == "safe"

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_functions_stream(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "What's the weather like today in Seattle?"}
        ]

        functions=[
            {
                "name": "get_current_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit to use. Infer this from the users location.",
                        },
                    },
                    "required": ["location"],
                },
            }
        ]

        response = await client_async.chat.completions.create(
            messages=messages,
            functions=functions,
            stream=True,
            **kwargs
        )
        args = ""
        async for completion in response:
            for c in completion.choices:
                assert c.delta is not None
                if c.delta.function_call:
                    if c.delta.function_call.name:
                        assert c.delta.function_call.name == "get_current_weather"
                    if c.delta.function_call.arguments:
                        args += c.delta.function_call.arguments
        assert "Seattle" in args

        messages.append(
            {
                "role": "function",
                "name": "get_current_weather",
                "content": "{\"temperature\": \"22\", \"unit\": \"celsius\", \"description\": \"Sunny\"}"
            }
        )
        function_completion = await client_async.chat.completions.create(
            messages=messages,
            functions=functions,
            stream=True,
            **kwargs
        )
        content = ""
        async for completion in function_completion:
            for c in completion.choices:
                assert c.delta is not None
                if c.delta.content:
                    content += c.delta.content
                if c.delta.role:
                    assert c.delta.role == "assistant"
        assert "sunny" in content.lower()
        assert "22" in content

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(AZURE, GA), (AZURE, PREVIEW), (OPENAI, "v1")]
    )
    async def test_chat_completion_given_function(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "What's the weather like today in Seattle?"}
        ]

        functions=[
            {
                "name": "get_current_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit to use. Infer this from the users location.",
                        },
                    },
                    "required": ["location"],
                },
            },
            {
                "name": "get_current_temperature",
                "description": "Get the current temperature",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit to use.",
                        },
                    },
                    "required": ["location"],
                },
            }
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            functions=functions,
            function_call={"name": "get_current_temperature"},
            **kwargs
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.role
        function_call =  completion.choices[0].message.function_call
        assert function_call.name == "get_current_temperature"
        assert "Seattle" in function_call.arguments

        messages.append(
            {
                "role": "function",
                "name": "get_current_temperature",
                "content": "{\"temperature\": \"22\", \"unit\": \"celsius\"}"
            }
        )
        function_completion = await client_async.chat.completions.create(
            messages=messages,
            functions=functions,
            **kwargs
        )
        assert function_completion
        assert "22" in function_completion.choices[0].message.content
        assert function_completion.choices[0].message.role == "assistant"

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, GA), (AZURE, PREVIEW)])
    async def test_chat_completion_functions_rai(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "how do I rob a bank with violence?"}
        ]

        functions=[
            {
                "name": "get_current_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "format": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "The temperature unit to use. Infer this from the users location.",
                        },
                    },
                    "required": ["location"],
                },
            }
        ]

        with pytest.raises(openai.BadRequestError) as e:
            response = await client_async.chat.completions.create(
                messages=messages,
                functions=functions,
                **kwargs
            )
        e = e.value
        assert e.code == "content_filter"
        assert e.message is not None
        assert e.status_code == 400
        err = e.body
        assert err["code"] == "content_filter"
        assert err["param"] == "prompt"
        assert err["message"] is not None
        content_filter_result = err["innererror"]["content_filter_result"]
        assert content_filter_result["hate"]["filtered"] is False
        assert content_filter_result["hate"]["severity"] == "safe"
        assert content_filter_result["self_harm"]["filtered"] is False
        assert content_filter_result["self_harm"]["severity"] == "safe"
        assert content_filter_result["sexual"]["filtered"] is False
        assert content_filter_result["sexual"]["severity"] == "safe"
        assert content_filter_result["violence"]["filtered"] is True
        assert content_filter_result["violence"]["severity"] is not None

        messages.append(
            {
                "role": "function",
                "name": "get_current_temperature",
                "content": "{\"temperature\": \"you can rob a bank by asking for the money\", \"unit\": \"celsius\"}"
            }
        )
        with pytest.raises(openai.BadRequestError) as e:
            function_completion = await client_async.chat.completions.create(
                messages=messages,
                functions=functions,
                **kwargs
            )
        e = e.value
        assert e.code == "content_filter"
        assert e.message is not None
        assert e.status_code == 400
        err = e.body
        assert err["code"] == "content_filter"
        assert err["param"] == "prompt"
        assert err["message"] is not None
        content_filter_result = err["innererror"]["content_filter_result"]
        assert content_filter_result["hate"]["filtered"] is False
        assert content_filter_result["hate"]["severity"] == "safe"
        assert content_filter_result["self_harm"]["filtered"] is False
        assert content_filter_result["self_harm"]["severity"] == "safe"
        assert content_filter_result["sexual"]["filtered"] is False
        assert content_filter_result["sexual"]["severity"] == "safe"
        assert content_filter_result["violence"]["filtered"] is True
        assert content_filter_result["violence"]["severity"] is not None

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, GA), (AZURE, PREVIEW)])
    async def test_chat_completion_byod(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What languages have libraries you know about for Azure OpenAI?"}
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            extra_body={
                "data_sources":[
                    {
                        "type": "azure_search",
                        "parameters": {
                            "endpoint": os.environ[ENV_AZURE_OPENAI_SEARCH_ENDPOINT],
                            "index_name": os.environ[ENV_AZURE_OPENAI_SEARCH_INDEX],
                            "authentication": {
                                "type": "system_assigned_managed_identity"
                            }
                        }
                    }
                ],
            },
            model="gpt-4-0613"
        )
        assert completion.id
        assert completion.object == "extensions.chat.completion"
        assert completion.model
        assert completion.created
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role
        assert completion.choices[0].message.context["citations"]
        assert completion.choices[0].message.context["intent"]

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, GA), (AZURE, PREVIEW)])
    async def test_streamed_chat_completions_byod(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What languages have libraries you know about for Azure OpenAI?"}
        ]

        response = await client_async.chat.completions.create(
            messages=messages,
            extra_body={
                "data_sources":[
                    {
                        "type": "azure_search",
                        "parameters": {
                            "endpoint": os.environ[ENV_AZURE_OPENAI_SEARCH_ENDPOINT],
                            "index_name": os.environ[ENV_AZURE_OPENAI_SEARCH_INDEX],
                            "authentication": {
                                "type": "system_assigned_managed_identity"
                            }
                        }
                    }
                ],
            },
            stream=True,
            model="gpt-4-0613"
        )
        async for chunk in response:
            assert chunk.id
            assert chunk.object == "extensions.chat.completion.chunk"
            assert chunk.created
            assert chunk.model
            for c in chunk.choices:
                assert c.index is not None
                assert c.delta is not None
                if hasattr(c.delta, "context"):
                    assert c.delta.context["citations"]
                    assert c.delta.context["intent"]
                if c.delta.role:
                    assert c.delta.role == "assistant"
                if c.delta.content:
                    assert c.delta.content is not None

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_seed(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Why is the sky blue?"}
        ]

        completion = await client_async.chat.completions.create(messages=messages, seed=42, **kwargs)
        if api_type != GPT_4_OPENAI:  # bug in openai where system_fingerprint is not always returned
            assert completion.system_fingerprint

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_json_response(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020? Return in json with answer as the key."}
        ]

        completion = await client_async.chat.completions.create(messages=messages, response_format={ "type": "json_object" }, **kwargs)
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert json.loads(completion.choices[0].message.content)
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, PREVIEW)])
    async def test_chat_completion_block_list_term(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the best time of year to pick pineapple?"}
        ]
        with pytest.raises(openai.BadRequestError) as e:
            await client_async.chat.completions.create(messages=messages, model="gpt-4-1106-preview")
        err = e.value.body
        assert err["code"] == "content_filter"
        content_filter_result = err["innererror"]["content_filter_result"]
        assert content_filter_result["custom_blocklists"]["filtered"] is True
        assert content_filter_result["custom_blocklists"]["details"][0]["id"].startswith("CustomBlockList")
        assert content_filter_result["hate"]["filtered"] is False
        assert content_filter_result["hate"]["severity"] == "safe"
        assert content_filter_result["self_harm"]["filtered"] is False
        assert content_filter_result["self_harm"]["severity"] == "safe"
        assert content_filter_result["sexual"]["filtered"] is False
        assert content_filter_result["sexual"]["severity"] == "safe"
        assert content_filter_result["violence"]["filtered"] is False
        assert content_filter_result["violence"]["severity"] == "safe"
        assert content_filter_result["profanity"]["detected"] is False
        assert content_filter_result["profanity"]["filtered"] is False
        assert content_filter_result["jailbreak"]["detected"] is False
        assert content_filter_result["jailbreak"]["filtered"] is False

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_tools(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into tools. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "What's the weather like today in Seattle?"}
        ]
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                        },
                        "required": ["location"],
                    },
                }
            }
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            tools=tools,
            tool_choice="auto",
            **kwargs
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.role
        function_call =  completion.choices[0].message.tool_calls[0].function
        assert function_call.name == "get_current_weather"
        assert "Seattle" in function_call.arguments
        messages.append(completion.choices[0].message)

        tool_call_id = completion.choices[0].message.tool_calls[0].id
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id,
                "content": "{\"temperature\": \"22\", \"unit\": \"celsius\", \"description\": \"Sunny\"}"
            }
        )
        tool_completion = await client_async.chat.completions.create(
            messages=messages,
            tools=tools,
            **kwargs
        )
        assert tool_completion
        assert "sunny" in tool_completion.choices[0].message.content.lower()
        assert "22" in tool_completion.choices[0].message.content
        assert tool_completion.choices[0].message.role == "assistant"

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_tools_stream(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into tools. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "What's the weather like today in Seattle?"}
        ]

        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                        },
                        "required": ["location"],
                    },
                }
            }
        ]
        response = await client_async.chat.completions.create(
            messages=messages,
            tools=tools,
            stream=True,
            **kwargs
        )
        args = ""
        async for completion in response:
            for c in completion.choices:
                assert c.delta is not None
                if c.delta.role:
                    assistant = c.delta.role
                if c.delta.tool_calls:
                    if c.delta.tool_calls[0].type:
                        tool_type = c.delta.tool_calls[0].type
                    if c.delta.tool_calls[0].id:
                        tool_id = c.delta.tool_calls[0].id
                    if c.delta.tool_calls[0].function.name:
                        function_name = c.delta.tool_calls[0].function.name
                    if c.delta.tool_calls[0].function.arguments:
                        args += c.delta.tool_calls[0].function.arguments
        assert "Seattle" in args

        assistant_message = {
            "role": assistant,
            "tool_calls": [
                {
                    "id": tool_id,
                    "type": tool_type,
                    "function": {
                        "name": function_name,
                        "arguments": args
                    }
                }
            ],
            "content": None
        }
        messages.append(assistant_message)
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_id,
                "content": "{\"temperature\": \"22\", \"unit\": \"celsius\", \"description\": \"Sunny\"}"
            }
        )
        function_completion = await client_async.chat.completions.create(
            messages=messages,
            tools=tools,
            stream=True,
            **kwargs
        )
        content = ""
        async for func in function_completion:
            for c in func.choices:
                assert c.delta is not None
                if c.delta.content:
                    content += c.delta.content
                if c.delta.role:
                    assert c.delta.role == "assistant"
        assert "sunny" in content.lower()
        assert "22" in content

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_tools_parallel_func(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into tools. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "What's the weather like today in Seattle and Los Angeles?"}
        ]
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                        },
                        "required": ["location"],
                    },
                }
            }
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            tools=tools,
            tool_choice="auto",
            **kwargs
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.role

        assert len(completion.choices[0].message.tool_calls) == 2
        messages.append(completion.choices[0].message)

        function_call = completion.choices[0].message.tool_calls[0].function
        assert function_call.name == "get_current_weather"
        assert "Seattle" in function_call.arguments
        tool_call_id_0 = completion.choices[0].message.tool_calls[0].id

        function_call = completion.choices[0].message.tool_calls[1].function
        assert function_call.name == "get_current_weather"
        assert "Los Angeles" in function_call.arguments
        tool_call_id_1 = completion.choices[0].message.tool_calls[1].id
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id_0,
                "content": "{\"temperature\": \"22\", \"unit\": \"celsius\", \"description\": \"Cloudy\"}"
            }
        )
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id_1,
                "content": "{\"temperature\": \"80\", \"unit\": \"fahrenheit\", \"description\": \"Sunny\"}"
            }
        )
        tool_completion = await client_async.chat.completions.create(
            messages=messages,
            tools=tools,
            **kwargs
        )
        assert tool_completion
        assert "sunny" in tool_completion.choices[0].message.content.lower()
        assert "cloudy" in tool_completion.choices[0].message.content.lower()
        assert "22" in tool_completion.choices[0].message.content
        assert "80" in tool_completion.choices[0].message.content
        assert tool_completion.choices[0].message.role == "assistant"

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_vision(self, client_async, api_type, api_version, **kwargs):
        completion = await client_async.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {"url": "https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/images/handwritten-note.jpg"}
                        },
                    ],
                }
            ],
        )
        assert completion.object == "chat.completion"
        assert len(completion.choices) == 1
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, PREVIEW), (GPT_4_AZURE, GA), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_logprobs(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            logprobs=True,
            top_logprobs=3,
            **kwargs
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role
        assert completion.choices[0].logprobs.content
        for logprob in completion.choices[0].logprobs.content:
            assert logprob.token is not None
            assert logprob.logprob is not None
            assert logprob.bytes is not None

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, PREVIEW), (GPT_4_AZURE, GA), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_structured_outputs(self, client_async, api_type, api_version, **kwargs):

        class Step(BaseModel):
            explanation: str
            output: str

        class MathResponse(BaseModel):
            steps: List[Step]
            final_answer: str

        completion = await client_async.beta.chat.completions.parse(
            messages=[
                {"role": "system", "content": "You are a helpful math tutor. You only answer about math. Refuse to answer any other question."},
                {"role": "user", "content": "solve 8x + 31 = 2"},
            ],
            response_format=MathResponse,
            **kwargs,
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role
        if completion.choices[0].message.parsed:
            assert completion.choices[0].message.parsed.steps
            for step in completion.choices[0].message.parsed.steps:
                assert step.explanation
                assert step.output
            assert completion.choices[0].message.parsed.final_answer

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize("api_type, api_version", [(GPT_4_AZURE, GA), (GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")])
    async def test_chat_completion_parallel_tool_calls_disable(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "system", "content": "Don't make assumptions about what values to plug into tools. Ask for clarification if a user request is ambiguous."},
            {"role": "user", "content": "What's the weather like today in Seattle and Los Angeles in Fahrenheit?"}
        ]
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                        },
                        "required": ["location"],
                    },
                }
            }
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            tools=tools,
            parallel_tool_calls=False,
            **kwargs
        )
        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.role
        assert len(completion.choices[0].message.tool_calls) == 1

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")]
    )
    async def test_chat_completion_token_details(self, client_async, api_type, api_version, **kwargs):
        messages = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the meaning of life?"}
        ]

        completion = await client_async.chat.completions.create(
            messages=messages,
            model="o1",
            reasoning_effort="low"
        )

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert completion.usage.completion_tokens_details
        assert completion.usage.completion_tokens_details.accepted_prediction_tokens is not None
        assert completion.usage.completion_tokens_details.audio_tokens is not None
        assert completion.usage.completion_tokens_details.reasoning_tokens is not None
        assert completion.usage.completion_tokens_details.rejected_prediction_tokens is not None
        assert completion.usage.prompt_tokens_details
        assert completion.usage.prompt_tokens_details.audio_tokens is not None
        assert completion.usage.prompt_tokens_details.cached_tokens is not None
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")]
    )
    async def test_chat_completion_audio_input(self, client_async, api_type, api_version, **kwargs):
        path = pathlib.Path(__file__)
        wav_file = path.parent / "assets" / "cat.wav"
        with open(wav_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode("utf-8")

        completion = await client_async.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "alloy", "format": "wav"},
            messages=[
                {
                    "role": "user",
                    "content": [
                        { 
                            "type": "text",
                            "text": "What is in this recording?"
                        },
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": encoded_string,
                                "format": "wav"
                            }
                        }
                    ]
                },
            ]
        )

        assert completion.choices[0]
        assert completion.choices[0].message.audio.data
        assert completion.choices[0].message.audio.transcript
        assert completion.usage.completion_tokens_details.audio_tokens is not None

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")]
    )
    async def test_chat_completion_audio_output(self, client_async, api_type, api_version, **kwargs):
        completion = await client_async.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "alloy", "format": "wav"},
            messages=[
                {
                    "role": "user",
                    "content": "Are bengals good cats? Keep it short."
                }
            ]
        )

        assert completion.choices[0]
        assert completion.choices[0].message.audio.data
        assert completion.choices[0].message.audio.transcript
        assert completion.usage.completion_tokens_details.audio_tokens is not None
        wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
        assert wav_bytes.startswith(b"RIFF")

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")]
    )
    async def test_chat_completion_predicted_outputs(self, client_async, api_type, api_version, **kwargs):

        code = """
        class User {
        firstName: string = "";
        lastName: string = "";
        username: string = "";
        }

        export default User;
        """

        refactor_prompt = """
        Replace the "username" property with an "email" property. Respond only 
        with code, and with no markdown formatting.
        """

        completion = await client_async.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": refactor_prompt
                },
                {
                    "role": "user",
                    "content": code
                }
            ],
            prediction={
                "type": "content",
                "content": code
            }
        )

        assert completion.id
        assert completion.object == "chat.completion"
        assert completion.model
        assert completion.created
        assert completion.usage.completion_tokens is not None
        assert completion.usage.prompt_tokens is not None
        assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
        assert completion.usage.completion_tokens_details
        assert completion.usage.completion_tokens_details.accepted_prediction_tokens is not None
        assert completion.usage.completion_tokens_details.audio_tokens is not None
        assert completion.usage.completion_tokens_details.reasoning_tokens is not None
        assert completion.usage.completion_tokens_details.rejected_prediction_tokens is not None
        assert completion.usage.prompt_tokens_details
        assert completion.usage.prompt_tokens_details.audio_tokens is not None
        assert completion.usage.prompt_tokens_details.cached_tokens is not None
        assert len(completion.choices) == 1
        assert completion.choices[0].finish_reason
        assert completion.choices[0].index is not None
        assert completion.choices[0].message.content is not None
        assert completion.choices[0].message.role

    @configure_async
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "api_type, api_version",
        [(GPT_4_AZURE, PREVIEW), (GPT_4_OPENAI, "v1")]
    )
    async def test_chat_completion_predicted_outputs_stream(self, client_async, api_type, api_version, **kwargs):

        code = """
        class User {
        firstName: string = "";
        lastName: string = "";
        username: string = "";
        }

        export default User;
        """

        refactor_prompt = """
        Replace the "username" property with an "email" property. Respond only 
        with code, and with no markdown formatting.
        """

        response = await client_async.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": refactor_prompt
                },
                {
                    "role": "user",
                    "content": code
                }
            ],
            prediction={
                "type": "content",
                "content": code
            },
            stream=True,
            stream_options={"include_usage": True}
        )
        async for completion in response:
            if len(completion.choices) > 0:
                assert completion.id
                assert completion.object == "chat.completion.chunk"
                assert completion.model
                assert completion.created
                for c in completion.choices:
                    assert c.index is not None
                    assert c.delta is not None
            if completion.usage:
                assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
                assert completion.usage.completion_tokens_details
                assert completion.usage.completion_tokens_details.accepted_prediction_tokens is not None
                assert completion.usage.completion_tokens_details.audio_tokens is not None
                assert completion.usage.completion_tokens_details.reasoning_tokens is not None
                assert completion.usage.completion_tokens_details.rejected_prediction_tokens is not None
                assert completion.usage.prompt_tokens_details
                assert completion.usage.prompt_tokens_details.audio_tokens is not None
                assert completion.usage.prompt_tokens_details.cached_tokens is not None
