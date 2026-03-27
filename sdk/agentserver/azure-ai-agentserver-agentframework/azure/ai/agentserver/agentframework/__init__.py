# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from ._version import VERSION


def from_agent_framework(agent):
    """
    Create an :class:`AgentServer` from a MAF ``AgentProtocol`` instance.

    Usage::

        from azure.ai.agentserver.agentframework import from_agent_framework
        server = from_agent_framework(agent)
        server.run()

    :param agent: An ``AgentProtocol`` instance (any object with ``.run()``).
    :returns: An :class:`AgentServer` ready to ``.run()``.
    """
    from azure.ai.agentserver.core import AgentServer

    from .invoke import create_invoke_handler

    invoke_fn = create_invoke_handler(agent)
    return AgentServer(invoke_fn=invoke_fn)


__all__ = ["from_agent_framework"]
__version__ = VERSION
