# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Simple mock agent that returns a canned response.

Demonstrates the minimal ``invoke(dict) -> dict`` contract
required by ``AgentServer``.
"""

from azure.ai.agentserver.core import AgentServer


async def invoke(request: dict) -> dict:
    """Handle an Invoke API request."""
    user_input = request.get("input", [])
    text = user_input[0] if user_input and isinstance(user_input[0], str) else "no input"

    return {
        "status": "completed",
        "message": f"I am a mock agent. You said: {text}",
        "annotations": [],
    }


server = AgentServer(invoke_fn=invoke)

if __name__ == "__main__":
    server.run()
