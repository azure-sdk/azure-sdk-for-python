# Azure AI Agent Server Adapter for Python


## Getting started

```bash
pip install azure-ai-agentserver-core
```

## Key concepts

This is the core package for the Azure AI Agent Server adapter.  It wraps your
agent as a container and exposes it over `POST /invoke` using the
[Invoke API](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/agentserver/invoke-api.md).

Your agent implements a single function — `invoke(request: dict) -> dict` — and
the `AgentServer` handles HTTP serving, JSON/SSE dispatch, health endpoints,
and OpenTelemetry tracing.


## Examples

### Minimal custom agent (no framework)

```python
from azure.ai.agentserver.core import AgentServer


async def invoke(request: dict) -> dict:
    """Handle an Invoke API request and return a response dict."""
    user_input = request.get("input", [])
    text = user_input[0] if isinstance(user_input[0], str) else user_input[0].get("content", "")

    return {
        "status": "completed",
        "message": f"Echo: {text}",
        "annotations": [],
    }


server = AgentServer(invoke_fn=invoke)

if __name__ == "__main__":
    server.run()  # starts on http://0.0.0.0:8080
```

### Loading from a module

```python
from azure.ai.agentserver.core import AgentServer

# Loads the `invoke` attribute from `my_agent.main`
server = AgentServer.from_module("my_agent.main")
server.run()
```

### Testing locally

```bash
# Non-streaming
curl -X POST http://localhost:8080/invoke \
  -H 'Content-Type: application/json' \
  -d '{"input": ["Hello!"]}'

# Streaming (auto-wrapped as SSE)
curl -N -X POST http://localhost:8080/invoke \
  -H 'Content-Type: application/json' \
  -d '{"input": ["Hello!"], "stream": true}'
```

## Troubleshooting

First run your agent with azure-ai-agentserver-core locally.

If it works locally but fails on cloud, check your logs in the Application
Insights instance connected to your Azure AI Foundry Project.


### Reporting issues

To report an issue with the client library, or request additional features,
please open a GitHub issue [here](https://github.com/Azure/azure-sdk-for-python/issues).
Mention the package name "azure-ai-agentserver" in the title or content.


## Next steps

Please visit the [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/agentserver/azure-ai-agentserver-core/samples)
folder for additional examples of building agents with azure-ai-agentserver.


## Contributing

This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct][code_of_conduct]. For more information,
see the Code of Conduct FAQ or contact opencode@microsoft.com with any
additional questions or comments.
