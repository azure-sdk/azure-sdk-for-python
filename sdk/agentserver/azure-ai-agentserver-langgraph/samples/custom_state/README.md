# Custom LangGraph State Sample (Mini RAG)

This sample demonstrates how to host a LangGraph agent **with a custom internal state** using the `azure.ai.agentserver` SDK.  It shows the minimal pattern required to adapt Invoke API requests to a LangGraph state and back to an Invoke API response dict.

## What It Shows
- Defining a custom state (`RAGState`) separate from the wire contract.
- Bridging Invoke API request dicts ↔ LangGraph state ↔ response dicts.
- A simple multi-step graph: intent analysis → optional retrieval → answer generation.
- Lightweight retrieval (keyword scoring over an in‑memory knowledge base) with citation annotations.
- Graceful local fallback answer when Azure OpenAI credentials are absent.

## Flow Overview
```
Invoke API request dict
  -> convert to RAGState
    -> LangGraph executes nodes (analyze → retrieve? → answer)
      -> Final state
        -> convert to Invoke API response dict
```

## Running
```
python main.py
```
Optional environment variables for live model call:
- AZURE_OPENAI_API_KEY
- AZURE_OPENAI_ENDPOINT (e.g. https://<your-project>.cognitiveservices.azure.com/)
- AZURE_AI_MODEL_DEPLOYMENT_NAME (model deployment name)

## Key Takeaway
A custom invoke handler is the seam where you map external Invoke API request dicts to an internal graph-friendly state shape and then format the final result back to an Invoke API response dict.  Start simple, then layer retrieval sophistication, memory, tools, and streaming as needed.
