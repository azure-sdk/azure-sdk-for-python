# Azure AI Agent Server Adapter for Agent Framework Python


## Getting started

```bash
pip install azure-ai-agentserver-agentframework
```


## Key concepts

This package wraps your Microsoft Agent Framework (MAF) agent and hosts it on
the cloud via `POST /invoke`.  You write your `AgentProtocol` agent as usual —
the adapter handles message conversion, interrupt detection, and Invoke API
response formatting automatically.


## Examples

```python
from my_framework_agent import my_awesome_agent

from azure.ai.agentserver.agentframework import from_agent_framework

if __name__ == "__main__":
    # One line — your agent is now hosted on http://localhost:8080/invoke
    from_agent_framework(my_awesome_agent).run()
```

### Testing locally

```bash
curl -X POST http://localhost:8080/invoke \
  -H 'Content-Type: application/json' \
  -d '{"input": ["Hello, agent!"]}'
```


## Troubleshooting

First run your agent with azure-ai-agentserver-agentframework locally.

If it works locally but fails on cloud, check your logs in the Application
Insights instance connected to your Azure AI Foundry Project.


## Next steps

Please visit the [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/agentserver/azure-ai-agentserver-agentframework/samples)
folder for examples of building agents with azure-ai-agentserver-* packages.


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
