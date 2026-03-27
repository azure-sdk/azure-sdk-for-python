# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from ._version import VERSION
from .logger import configure as config_logging
from .server.agent_server import AgentServer, get_platform_context

config_logging()

__all__ = ["AgentServer", "get_platform_context"]
__version__ = VERSION
