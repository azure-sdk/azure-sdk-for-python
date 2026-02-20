# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Minimal agent — raw invoke() function, no framework dependencies.

Demonstrates:
  - Non-streaming response (dict return)
  - Streaming response (async generator)
  - Zero framework imports — only AgentServer from core
"""
from azure.ai.agentserver.core import AgentServer


async def invoke(request: dict):
    """
    The simplest possible invoke function.

    - If ``stream`` is true, yields word-by-word deltas.
    - Otherwise returns a complete response dict.
    """
    input_items = request.get("input", [])
    # Extract user text from the first input item
    user_text = ""
    for item in input_items:
        if isinstance(item, str):
            user_text = item
            break
        if isinstance(item, dict):
            user_text = item.get("text", "") or item.get("content", "")
            if isinstance(user_text, list):
                user_text = " ".join(p.get("text", "") for p in user_text if isinstance(p, dict))
            break

    reply = f"Echo: {user_text}" if user_text else "Hello! Send me a message."

    if request.get("stream"):
        return _stream_reply(reply)

    return {
        "status": "completed",
        "message": reply,
        "annotations": [],
    }


async def _stream_reply(text: str):
    """Yield word-by-word deltas, then a terminal event."""
    words = text.split()
    for i, word in enumerate(words):
        suffix = " " if i < len(words) - 1 else ""
        yield {"type": "message.delta", "delta": word + suffix}
    yield {
        "type": "invocation.completed",
        "status": "completed",
        "message": text,
        "annotations": [],
    }


if __name__ == "__main__":
    server = AgentServer(invoke_fn=invoke)
    server.run()
