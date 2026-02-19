# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Thin LangGraph wrapper for the Invoke API.

Converts between Invoke API dicts and LangChain message types,
then delegates to the compiled LangGraph ``StateGraph``.

Usage::

    from langgraph.graph.state import CompiledStateGraph
    from azure.ai.agentserver.langgraph import from_langgraph

    graph: CompiledStateGraph = build_my_graph()
    server = from_langgraph(graph)
    server.run()
"""
from __future__ import annotations

import os
from typing import AsyncGenerator, Optional

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langgraph.graph.state import CompiledStateGraph

from azure.ai.agentserver.core.logger import get_logger

logger = get_logger()


def create_invoke_handler(
    graph: CompiledStateGraph,
    *,
    default_thread_id: str = "default",
):
    """
    Return an ``invoke(dict) -> dict | AsyncGenerator`` function
    that wraps a compiled LangGraph.

    :param graph: A compiled LangGraph state graph.
    :param default_thread_id: Thread ID to use when ``session_id`` is absent.
    """

    async def invoke(request: dict):
        messages = _to_langchain_messages(request.get("input", []))
        thread_id = request.get("session_id") or default_thread_id
        config = {"configurable": {"thread_id": thread_id}}

        # Add LangSmith/Azure AI callbacks if tracing is configured
        callbacks = _get_callbacks()
        if callbacks:
            config["callbacks"] = callbacks

        if request.get("stream"):
            return _stream(graph, messages, config)

        result = await graph.ainvoke({"messages": messages}, config=config)
        last_ai = _last_ai_message(result.get("messages", []))
        return {
            "status": "completed",
            "message": last_ai.content if last_ai else "",
            "annotations": [],
        }

    return invoke


async def _stream(
    graph: CompiledStateGraph,
    messages: list[BaseMessage],
    config: dict,
) -> AsyncGenerator[dict, None]:
    """Stream LangGraph output as Invoke API SSE dicts."""
    try:
        async for chunk, metadata in graph.astream(
            {"messages": messages},
            config=config,
            stream_mode="messages",
        ):
            if isinstance(chunk, AIMessage) and chunk.content and not chunk.tool_calls:
                yield {"type": "message.delta", "delta": chunk.content}
    except Exception as exc:
        logger.error("LangGraph streaming error: %s", exc)
        yield {
            "type": "error",
            "code": "agent_error",
            "message": str(exc),
        }
        return

    yield {"type": "invocation.completed", "status": "completed"}


# ------------------------------------------------------------------
# Message conversion helpers
# ------------------------------------------------------------------

_ROLE_MAP = {
    "user": HumanMessage,
    "system": SystemMessage,
    "assistant": AIMessage,
}


def _to_langchain_messages(input_items: list) -> list[BaseMessage]:
    """Convert Invoke API ``input`` list to LangChain messages."""
    messages: list[BaseMessage] = []
    for item in input_items:
        if isinstance(item, str):
            messages.append(HumanMessage(content=item))
            continue

        role = item.get("role", "user")
        msg_cls = _ROLE_MAP.get(role, HumanMessage)

        # Handle both flat text and structured content
        content = item.get("content") or item.get("text", "")
        if isinstance(content, list):
            # Extract text parts from content list
            text_parts = [
                part.get("text", "") for part in content if part.get("type") == "input_text" or part.get("text")
            ]
            content = " ".join(text_parts)
        elif item.get("type") == "text":
            content = item.get("text", "")

        if content:
            messages.append(msg_cls(content=content))

    return messages


def _last_ai_message(messages: list) -> Optional[AIMessage]:
    """Return the last AIMessage that isn't a tool call."""
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and msg.content and not msg.tool_calls:
            return msg
    return None


def _get_callbacks() -> list | None:
    """Build tracing callbacks if configured."""
    callbacks = []
    app_insights = os.environ.get("_AGENT_RUNTIME_APP_INSIGHTS_CONNECTION_STRING")
    if app_insights:
        try:
            from langchain_azure_ai.callbacks.tracers import AzureAIOpenTelemetryTracer

            tracer = AzureAIOpenTelemetryTracer(
                connection_string=app_insights,
                enable_content_recording=True,
                name=os.getenv("AGENT_NAME", "HostedAgent-LangGraph"),
            )
            callbacks.append(tracer)
        except ImportError:
            pass

    return callbacks or None
