# MAF (Microsoft Agent Framework) Agent

A MAF-based agent using `from_agent_framework()` for zero-boilerplate serving.

## Run

```bash
pip install azure-ai-agentserver-agentframework
python main.py
```

The server starts on `http://0.0.0.0:8080`.

## Test

### Non-streaming

```bash
curl -s -X POST http://localhost:8080/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": [{"type": "text", "text": "Hello from MAF"}]}'
```

Expected:

```json
{"status": "completed", "message": "MAF Echo: Hello from MAF", "annotations": []}
```

### Health

```bash
curl http://localhost:8080/liveness
```
