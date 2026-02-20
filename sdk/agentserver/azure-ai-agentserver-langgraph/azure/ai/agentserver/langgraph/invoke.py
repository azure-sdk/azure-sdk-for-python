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
from typing import Optional

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
    Return an ``invoke(dict) -> dict`` function that wraps a compiled LangGraph.

    Always returns a dict. The server auto-wraps as SSE when the caller
    requests streaming. No branching on ``stream`` here.

    :param graph: A compiled LangGraph state graph.
    :param default_thread_id: Thread ID to use when ``session_id`` is absent.
    """

    async def invoke(request: dict) -> dict:
        messages = _to_langchain_messages(request.get("input", []))
        thread_id = request.get("session_id") or default_thread_id
        config = {"configurable": {"thread_id": thread_id}}

        # Add LangSmith/Azure AI callbacks if tracing is configured
        callbacks = _get_callbacks()
        if callbacks:
            config["callbacks"] = callbacks

        result = await graph.ainvoke({"messages": messages}, config=config)
        last_ai = _last_ai_message(result.get("messages", []))
        return {
            "status": "completed",
            "message": last_ai.content if last_ai else "",
            "annotations": [],
        }

    return invoke


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
