# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
MAF (Microsoft Agent Framework) agent — demonstrates from_agent_framework() wrapper.

Requires: pip install azure-ai-agentserver-agentframework
"""
from azure.ai.agentserver.agentframework import from_agent_framework

from agent import create_agent


if __name__ == "__main__":
    agent = create_agent()
    server = from_agent_framework(agent)
    server.run()
