# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
LangGraph agent — demonstrates from_langgraph() wrapper.

A simple ReAct-style agent with a mock tool.
Requires: pip install azure-ai-agentserver-langgraph
"""
from azure.ai.agentserver.langgraph import from_langgraph

from agent import build_graph


if __name__ == "__main__":
    graph = build_graph()
    server = from_langgraph(graph)
    server.run()
