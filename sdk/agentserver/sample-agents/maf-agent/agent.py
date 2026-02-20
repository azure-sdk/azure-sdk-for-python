# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Agent definition — a minimal MAF agent that echoes user input.

This uses the AgentProtocol interface from agent_framework.
"""
from agent_framework import Agent, ChatMessage, Role
from agent_framework._types import TextContent


class EchoAgent(Agent):
    """A simple echo agent for demonstration purposes."""

    async def run(self, message):
        """Process a message and return a response."""
        # Extract text from input
        if isinstance(message, str):
            user_text = message
        elif isinstance(message, ChatMessage):
            user_text = " ".join(
                c.text for c in (message.contents or []) if hasattr(c, "text") and c.text
            )
        elif isinstance(message, list):
            parts = []
            for m in message:
                if isinstance(m, str):
                    parts.append(m)
                elif isinstance(m, ChatMessage):
                    parts.extend(
                        c.text for c in (m.contents or []) if hasattr(c, "text") and c.text
                    )
            user_text = " ".join(parts)
        else:
            user_text = str(message)

        reply = f"MAF Echo: {user_text}" if user_text else "Hello from MAF agent!"

        # Return an AgentRunResponse-compatible object
        response_msg = ChatMessage(
            role=Role.ASSISTANT,
            contents=[TextContent(text=reply)],
        )
        return _SimpleResponse([response_msg])


class _SimpleResponse:
    """Minimal response object matching AgentRunResponse interface."""

    def __init__(self, messages):
        self.messages = messages


def create_agent():
    """Create and return the echo agent."""
    return EchoAgent()
