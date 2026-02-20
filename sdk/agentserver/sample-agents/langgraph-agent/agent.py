# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Graph definition — a minimal LangGraph agent with a greet tool.
"""
from langchain_core.messages import AIMessage
from langgraph.graph import MessagesState, StateGraph


def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to the Hosted Agents platform."


def chatbot(state: MessagesState):
    """Simple chatbot node — echoes back with a greeting."""
    last_msg = state["messages"][-1]
    user_text = last_msg.content if hasattr(last_msg, "content") else str(last_msg)

    # Simple logic: if the user says a name, greet them
    if user_text.strip():
        reply = greet(user_text.strip())
    else:
        reply = "Hi there! Tell me your name and I'll greet you."

    return {"messages": [AIMessage(content=reply)]}


def build_graph():
    """Build and compile the LangGraph state graph."""
    graph = StateGraph(MessagesState)
    graph.add_node("chatbot", chatbot)
    graph.set_entry_point("chatbot")
    graph.set_finish_point("chatbot")
    return graph.compile()
