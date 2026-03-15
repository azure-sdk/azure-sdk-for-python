# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Utility to load an ``invoke()`` function from a dotted module path
using :func:`importlib.import_module`.

Usage::

    fn = load_invoke_fn("my_agent.main", attr="invoke")
    result = fn({"input": [{"type": "text", "text": "hi"}]})
"""
import importlib
import inspect


def load_invoke_fn(module_path: str, attr: str = "invoke"):
    """
    Import *module_path* and return ``getattr(module, attr)``.

    Validates that the attribute exists and is callable.

    :param module_path: Dotted Python module path (e.g. ``my_agent.main``).
    :param attr: Name of the callable inside the module.  Default ``"invoke"``.
    :returns: The callable.
    :raises ImportError: If the module cannot be imported.
    :raises AttributeError: If the module has no such attribute.
    :raises TypeError: If the attribute is not callable.
    """
    mod = importlib.import_module(module_path)
    if not hasattr(mod, attr):
        raise AttributeError(f"Module '{module_path}' has no attribute '{attr}'")

    fn = getattr(mod, attr)
    if not callable(fn):
        raise TypeError(f"'{module_path}.{attr}' is not callable")

    kind = "async" if inspect.iscoroutinefunction(fn) or inspect.isasyncgenfunction(fn) else "sync"
    gen = " generator" if inspect.isgeneratorfunction(fn) or inspect.isasyncgenfunction(fn) else ""
    from ..logger import get_logger

    logger = get_logger()
    logger.info(f"Loaded {kind}{gen} invoke function from {module_path}.{attr}")
    return fn
