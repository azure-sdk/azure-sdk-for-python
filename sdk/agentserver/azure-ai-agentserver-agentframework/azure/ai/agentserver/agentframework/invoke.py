# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Thin MAF (Microsoft Agent Framework) wrapper for the Invoke API.

Converts between Invoke API dicts and ``agent_framework`` types,
then delegates to the ``AgentProtocol`` instance.

Usage::

    from agent_framework import Agent  # or any AgentProtocol impl
    from azure.ai.agentserver.agentframework import from_agent_framework

    agent = MyAgent()
    server = from_agent_framework(agent)
    server.run()
"""
from __future__ import annotations

import os
from typing import Any, AsyncGenerator, Optional

from azure.ai.agentserver.core.logger import get_logger

logger = get_logger()


def create_invoke_handler(agent: Any):
    """
    Return an ``invoke(dict) -> dict | AsyncGenerator`` function
    that wraps a MAF ``AgentProtocol`` agent.

    :param agent: An ``AgentProtocol`` instance (any object with ``.run()`` / ``.run_stream()``).
    """

    async def invoke(request: dict):
        input_items = request.get("input", [])
        message = _to_maf_input(input_items)
        stream = request.get("stream", False)

        # Handle resume (human-in-the-loop)
        resume = request.get("resume")
        if resume:
            message = _build_resume_input(resume, message)

        if stream and hasattr(agent, "run_stream"):
            return _stream(agent, message)

        # Non-streaming
        result = await agent.run(message)
        return _response_from_result(result)

    return invoke


async def _stream(agent: Any, message: Any) -> AsyncGenerator[dict, None]:
    """Stream MAF output as Invoke API SSE dicts."""
    try:
        full_text_parts: list[str] = []
        async for update in agent.run_stream(message):
            text = _extract_text(update)
            if text:
                full_text_parts.append(text)
                yield {"type": "message.delta", "delta": text}

            # Check for interrupt/human-in-the-loop
            interrupt = _extract_interrupt(update)
            if interrupt:
                yield {"type": "interrupt", **interrupt}
    except Exception as exc:
        logger.error("MAF streaming error: %s", exc)
        yield {"type": "error", "code": "agent_error", "message": str(exc)}
        return

    yield {
        "type": "invocation.completed",
        "status": "completed",
        "message": "".join(full_text_parts),
        "annotations": [],
    }


def _response_from_result(result: Any) -> dict:
    """Convert a MAF ``AgentRunResponse`` to an Invoke API response dict."""
    text_parts: list[str] = []
    annotations: list[dict] = []
    interrupt: Optional[dict] = None

    messages = getattr(result, "messages", [])
    for msg in messages:
        contents = getattr(msg, "contents", None)
        if not contents:
            continue
        for content in contents:
            text = _extract_text_from_content(content)
            if text:
                text_parts.append(text)

            intr = _extract_interrupt_from_content(content)
            if intr:
                interrupt = intr

    status = "requires_input" if interrupt else "completed"
    response: dict = {
        "status": status,
        "message": " ".join(text_parts),
        "annotations": annotations,
    }
    if interrupt:
        response["interrupt"] = interrupt
    return response


# ------------------------------------------------------------------
# Input conversion helpers
# ------------------------------------------------------------------

def _to_maf_input(input_items: list) -> Any:
    """Convert Invoke API ``input`` list to MAF input."""
    try:
        from agent_framework import ChatMessage, Role as ChatRole
        from agent_framework._types import TextContent

        messages: list[ChatMessage] = []
        for item in input_items:
            if isinstance(item, str):
                messages.append(ChatMessage(role=ChatRole.USER, contents=[TextContent(text=item)]))
                continue

            role_str = item.get("role", "user")
            role_map = {
                "user": ChatRole.USER,
                "assistant": ChatRole.ASSISTANT,
                "system": ChatRole.SYSTEM,
            }
            role = role_map.get(role_str, ChatRole.USER)

            # Extract text from various input formats
            text = _extract_input_text(item)
            if text:
                messages.append(ChatMessage(role=role, contents=[TextContent(text=text)]))

        # Return single message or list
        if len(messages) == 1:
            return messages[0]
        return messages or None
    except ImportError:
        # Fallback if agent_framework types aren't available
        texts = [_extract_input_text(item) for item in input_items]
        return " ".join(t for t in texts if t)


def _extract_input_text(item: Any) -> str:
    """Extract text from an Invoke API input item."""
    if isinstance(item, str):
        return item

    # Simple text item: {"type": "text", "text": "..."}
    if item.get("type") == "text":
        return item.get("text", "")

    # Content-based: {"content": "..."} or {"content": [{"type": "input_text", "text": "..."}]}
    content = item.get("content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [p.get("text", "") for p in content if isinstance(p, dict)]
        return " ".join(parts)

    return str(item.get("text", ""))


def _build_resume_input(resume: dict, original_message: Any) -> Any:
    """Build MAF input for a resume (human-in-the-loop continuation)."""
    try:
        from agent_framework import ChatMessage, FunctionResultContent, Role as ChatRole

        # The resume dict contains the function result that the human provided
        func_name = resume.get("function_name", "unknown")
        call_id = resume.get("call_id", "")
        result_val = resume.get("result", "")
        return ChatMessage(
            role=ChatRole.USER,
            contents=[FunctionResultContent(name=func_name, call_id=call_id, result=result_val)],
        )
    except ImportError:
        return original_message


# ------------------------------------------------------------------
# Output extraction helpers
# ------------------------------------------------------------------

def _extract_text(update: Any) -> Optional[str]:
    """Extract text from a MAF streaming update."""
    # Try direct content attribute
    if hasattr(update, "content") and isinstance(update.content, str):
        return update.content

    # Try contents list
    contents = getattr(update, "contents", None)
    if contents:
        for content in contents:
            text = _extract_text_from_content(content)
            if text:
                return text
    return None


def _extract_text_from_content(content: Any) -> Optional[str]:
    """Extract text from a MAF content item."""
    type_name = type(content).__name__
    if type_name == "TextContent" or hasattr(content, "text"):
        text = getattr(content, "text", None)
        return text if text else None
    return None


def _extract_interrupt(update: Any) -> Optional[dict]:
    """Extract interrupt info from a MAF streaming update."""
    contents = getattr(update, "contents", None)
    if contents:
        for content in contents:
            intr = _extract_interrupt_from_content(content)
            if intr:
                return intr
    return None


def _extract_interrupt_from_content(content: Any) -> Optional[dict]:
    """Extract interrupt info from a MAF content item."""
    type_name = type(content).__name__
    if type_name == "FunctionCallContent":
        return {
            "id": getattr(content, "call_id", ""),
            "message": f"Function call: {getattr(content, 'name', 'unknown')}",
            "function_name": getattr(content, "name", "unknown"),
            "arguments": getattr(content, "arguments", {}),
        }
    return None
