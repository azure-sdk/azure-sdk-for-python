# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from ._version import VERSION


def from_langgraph(graph, **kwargs):
    """
    Create an :class:`AgentServer` from a compiled LangGraph state graph.

    Usage::

        from azure.ai.agentserver.langgraph import from_langgraph
        server = from_langgraph(graph)
        server.run()

    :param graph: A ``CompiledStateGraph`` instance.
    :returns: An :class:`AgentServer` ready to ``.run()``.
    """
    from azure.ai.agentserver.core import AgentServer

    from .invoke import create_invoke_handler

    invoke_fn = create_invoke_handler(graph, **kwargs)
    return AgentServer(invoke_fn=invoke_fn)


__all__ = ["from_langgraph"]
__version__ = VERSION
