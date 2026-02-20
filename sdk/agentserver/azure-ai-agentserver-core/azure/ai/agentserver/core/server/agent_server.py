# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
AgentServer — the operational runtime for Hosted Agents.

Loads an ``invoke(request: dict) -> dict | AsyncGenerator[dict]`` function
and exposes it over HTTP via ``POST /invoke``.  Dict returns become JSON
responses; async-generator returns become SSE streams.

Usage::

    from azure.ai.agentserver.core import AgentServer

    server = AgentServer(invoke_fn=my_invoke)
    server.run()                 # starts HTTP on 0.0.0.0:8080

    # or load from a module
    server = AgentServer.from_module("my_agent", attr="invoke")
    server.run()
"""
import asyncio
import inspect
import json
import os
import traceback
from typing import Any, AsyncGenerator, Callable, Generator, Optional, Union

import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, StreamingResponse
from starlette.routing import Route

from ..constants import Constants
from ..logger import get_logger, request_context

logger = get_logger()
DEBUG_ERRORS = os.environ.get(Constants.AGENT_DEBUG_ERRORS, "false").lower() == "true"

InvokeFn = Callable[[dict], Union[dict, AsyncGenerator[dict, None], Generator[dict, None, None]]]


class AgentServer:
    """
    HTTP server that wraps an ``invoke()`` function behind ``POST /invoke``.

    The invoke function receives the Invoke API request dict and returns either:
    - A dict (non-streaming) → serialised as ``JSONResponse``
    - An async generator of dicts (streaming) → serialised as SSE
    - A sync generator of dicts (streaming) → wrapped in async, then SSE

    Sync invoke functions are automatically run in a thread via
    ``asyncio.to_thread`` so the event loop is never blocked.
    """

    def __init__(self, invoke_fn: Optional[InvokeFn] = None):
        """
        :param invoke_fn: A callable ``(dict) -> dict | generator``.
        """
        self.invoke_fn = invoke_fn
        self._is_async = invoke_fn is not None and (
            inspect.iscoroutinefunction(invoke_fn) or inspect.isasyncgenfunction(invoke_fn)
        )
        self._is_sync_gen = invoke_fn is not None and inspect.isgeneratorfunction(invoke_fn)

        routes = [
            Route("/invoke", self._invoke_endpoint, methods=["POST"]),
            Route("/liveness", self._health, methods=["GET"]),
            Route("/readiness", self._health, methods=["GET"]),
        ]
        self.app = Starlette(routes=routes)
        self.tracer = None

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------
    @classmethod
    def from_module(cls, module_path: str, attr: str = "invoke") -> "AgentServer":
        """
        Load an invoke function from a dotted module path.

        Example::

            server = AgentServer.from_module("my_agent.main", attr="invoke")

        :param module_path: Dotted Python module path (e.g. ``my_agent.main``).
        :param attr: Name of the callable inside the module. Default ``"invoke"``.
        """
        from .invoke_loader import load_invoke_fn

        fn = load_invoke_fn(module_path, attr)
        return cls(invoke_fn=fn)

    # ------------------------------------------------------------------
    # Endpoints
    # ------------------------------------------------------------------
    async def _invoke_endpoint(self, request: Request):
        """``POST /invoke`` — deserialise JSON, call invoke, dispatch result."""
        if self.invoke_fn is None:
            return JSONResponse(
                {"status": "failed", "error": {"code": "no_invoke_fn", "message": "No invoke function configured"}},
                status_code=500,
            )

        try:
            body = await request.json()
        except Exception as exc:
            logger.error("Invalid JSON payload: %s", exc)
            return JSONResponse(
                {"status": "failed", "error": {"code": "invalid_json", "message": str(exc)}},
                status_code=400,
            )

        # Set request context for logging/tracing
        self._set_request_context(request, body)
        caller_wants_stream = body.get("stream", False)

        try:
            result = await self._call_invoke(body)
            return self._dispatch(result, caller_wants_stream)
        except Exception as exc:
            err_msg = str(exc) if DEBUG_ERRORS else "Internal error"
            logger.error("Error in invoke: %s\n%s", exc, traceback.format_exc())
            return JSONResponse(
                {"status": "failed", "error": {"code": "invocation_error", "message": err_msg}},
                status_code=500,
            )

    async def _health(self, request: Request):
        """``GET /liveness`` and ``GET /readiness``."""
        return JSONResponse({"status": "ok"})

    # ------------------------------------------------------------------
    # Invoke dispatch
    # ------------------------------------------------------------------
    async def _call_invoke(self, request: dict) -> Any:
        """Call the invoke function, handling sync/async transparently."""
        if self._is_async:
            return await self.invoke_fn(request)
        if self._is_sync_gen:
            # Wrap sync generator → async generator
            return self._wrap_sync_generator(self.invoke_fn(request))
        # Plain sync function → run in thread
        return await asyncio.to_thread(self.invoke_fn, request)

    def _dispatch(self, result: Any, caller_wants_stream: bool = False):
        """Route the invoke result to the correct HTTP response type.

        The invoke function returns ONE shape — either a dict or a generator.
        The server adapts to what the caller wants:

        - dict + non-streaming caller → JSONResponse
        - dict + streaming caller → auto-wrap as single ``invocation.completed`` SSE event
        - generator → SSE stream (regardless of caller preference)

        This means the customer never needs to branch on ``stream``.
        They implement one return type; the server handles both callers.
        """
        if isinstance(result, dict):
            if caller_wants_stream:
                # Auto-wrap dict as a single-event SSE stream
                return StreamingResponse(
                    self._dict_to_stream(result),
                    media_type="text/event-stream",
                )
            return JSONResponse(result)
        if inspect.isasyncgen(result) or inspect.isgenerator(result):
            gen = result if inspect.isasyncgen(result) else self._wrap_sync_generator(result)
            if not caller_wants_stream:
                # Caller wants JSON but invoke returned a generator —
                # we can't easily collapse a stream, so serve SSE anyway.
                # The caller should handle this gracefully.
                pass
            return StreamingResponse(
                self._stream_with_prefetch(gen),
                media_type="text/event-stream",
            )
        # Fallback — try to serialise whatever we got
        return JSONResponse(result)

    @staticmethod
    async def _dict_to_stream(result: dict):
        """Wrap a dict response as a single SSE ``invocation.completed`` event."""
        event = {**result, "type": result.get("type", "invocation.completed")}
        yield _event_to_sse(event)
        yield "data: [DONE]\n\n"

    async def _stream_with_prefetch(self, gen: AsyncGenerator[dict, None]):
        """
        Yield SSE chunks from an async generator.

        Prefetches the first event so that errors during initialisation
        can surface as HTTP 500 *before* headers are sent.  After headers
        are committed, errors are sent as ``event: error`` SSE events.
        """
        try:
            first = await gen.__anext__()
        except StopAsyncIteration:
            yield "data: [DONE]\n\n"
            return
        # If __anext__ raises any other exception it propagates up and
        # Starlette returns a 500 before committing headers.

        error_sent = False
        try:
            yield _event_to_sse(first)
            async for event in gen:
                yield _event_to_sse(event)
        except Exception as exc:
            err_msg = str(exc) if DEBUG_ERRORS else "Internal error"
            logger.error("Streaming error: %s\n%s", exc, traceback.format_exc())
            payload = {"type": "error", "code": "stream_error", "message": err_msg}
            yield f"event: error\ndata: {json.dumps(payload)}\n\n"
            error_sent = True
        finally:
            if not error_sent:
                yield "data: [DONE]\n\n"

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    @staticmethod
    async def _wrap_sync_generator(gen: Generator) -> AsyncGenerator:
        """Wrap a synchronous generator as an async generator."""
        loop = asyncio.get_event_loop()
        sentinel = object()
        while True:
            item = await loop.run_in_executor(None, next, gen, sentinel)
            if item is sentinel:
                break
            yield item

    def _set_request_context(self, request: Request, body: dict):
        """Populate the context var used by the logger for structured fields."""
        ctx = request_context.get() or {}
        request_id = request.headers.get("X-Request-Id")
        if request_id:
            ctx["azure.ai.agentserver.x-request-id"] = request_id
        ctx["azure.ai.agentserver.session_id"] = body.get("session_id", "")
        ctx["azure.ai.agentserver.streaming"] = str(body.get("stream", False))
        request_context.set(ctx)

    # ------------------------------------------------------------------
    # Tracing
    # ------------------------------------------------------------------
    def init_tracing(self):
        """Set up OpenTelemetry tracing if exporters are configured."""
        from opentelemetry import trace

        exporter = os.environ.get(Constants.OTEL_EXPORTER_ENDPOINT)
        app_insights = os.environ.get(Constants.APPLICATION_INSIGHTS_CONNECTION_STRING)
        if exporter or app_insights:
            from opentelemetry.sdk.resources import Resource
            from opentelemetry.sdk.trace import TracerProvider

            resource = Resource.create({"service.name": "azure.ai.agentserver"})
            provider = TracerProvider(resource=resource)
            if exporter:
                self._setup_otlp(exporter, provider)
            if app_insights:
                self._setup_appinsights(app_insights, provider)
            trace.set_tracer_provider(provider)
        self.tracer = trace.get_tracer(__name__)

    @staticmethod
    def _setup_otlp(endpoint: str, provider):
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))
        logger.info("Tracing: OTLP exporter → %s", endpoint)

    @staticmethod
    def _setup_appinsights(conn_str: str, provider):
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

        exporter = AzureMonitorTraceExporter.from_connection_string(conn_str)
        provider.add_span_processor(BatchSpanProcessor(exporter))
        logger.info("Tracing: Application Insights exporter configured.")

    # ------------------------------------------------------------------
    # Server lifecycle
    # ------------------------------------------------------------------
    def run(self, host: str = "0.0.0.0", port: int = int(os.environ.get("DEFAULT_AD_PORT", "8080"))) -> None:
        """
        Start the HTTP server (blocking).

        :param host: Bind address.  Default ``0.0.0.0``.
        :param port: Port.  Default ``8080`` (or ``$DEFAULT_AD_PORT``).
        """
        self.init_tracing()
        logger.info("Starting AgentServer on %s:%d", host, port)
        uvicorn.run(self.app, host=host, port=port)

    async def run_async(self, host: str = "0.0.0.0", port: int = int(os.environ.get("DEFAULT_AD_PORT", "8080"))) -> None:
        """
        Awaitable server start for use inside an existing event loop.
        """
        self.init_tracing()
        config = uvicorn.Config(self.app, host=host, port=port, loop="asyncio")
        server = uvicorn.Server(config)
        logger.info("Starting AgentServer async on %s:%d", host, port)
        await server.serve()


# ------------------------------------------------------------------
# Module-level helpers
# ------------------------------------------------------------------
def _event_to_sse(event: dict) -> str:
    """Format a dict as an SSE chunk.  Uses ``event:`` field if present."""
    data = json.dumps(event)
    event_type = event.get("type")
    if event_type:
        return f"event: {event_type}\ndata: {data}\n\n"
    return f"data: {data}\n\n"
