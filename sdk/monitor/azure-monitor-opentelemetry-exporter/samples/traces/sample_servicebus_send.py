# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Examples to show usage of the azure-core-tracing-opentelemetry
with the servicebus SDK and exporting to Azure monitor backend.

This example traces calls for sending messages to the servicebus queue.

The telemetry will be collected automatically and sent to Application
Insights via the AzureMonitorTraceExporter
"""
# mypy: disable-error-code="attr-defined"
import os

# Declare OpenTelemetry as enabled tracing plugin for Azure SDKs
from azure.core.settings import settings
from azure.core.tracing.ext.opentelemetry_span import OpenTelemetrySpan

settings.tracing_implementation = OpenTelemetrySpan

# Regular open telemetry usage from here, see https://github.com/open-telemetry/opentelemetry-python
# for details
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# azure monitor trace exporter to send telemetry to appinsights
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

span_processor = BatchSpanProcessor(
    AzureMonitorTraceExporter.from_connection_string(os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"])
)
trace.get_tracer_provider().add_span_processor(span_processor)

# Example with Servicebus SDKs
from azure.servicebus import ServiceBusClient, ServiceBusMessage

connstr = os.environ["SERVICE_BUS_CONN_STR"]
queue_name = os.environ["SERVICE_BUS_QUEUE_NAME"]

with tracer.start_as_current_span(name="MyApplication"):
    with ServiceBusClient.from_connection_string(connstr) as client:
        with client.get_queue_sender(queue_name) as sender:
            # Sending a single message
            single_message = ServiceBusMessage("Single message")
            sender.send_messages(single_message)

            # Sending a list of messages
            messages = [ServiceBusMessage("First message"), ServiceBusMessage("Second message")]
            sender.send_messages(messages)
