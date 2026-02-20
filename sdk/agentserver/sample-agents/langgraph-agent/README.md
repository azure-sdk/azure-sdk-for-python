# LangGraph Agent

A LangGraph-based agent using `from_langgraph()` for zero-boilerplate serving.

## Run

```bash
pip install azure-ai-agentserver-langgraph
python main.py
```

The server starts on `http://0.0.0.0:8080`.

## Test

### Non-streaming

```bash
curl -s -X POST http://localhost:8080/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": [{"type": "text", "text": "Alice"}]}'
```

Expected:

```json
{"status": "completed", "message": "Hello, Alice! Welcome to the Hosted Agents platform.", "annotations": []}
```

### Streaming

```bash
curl -s -N -X POST http://localhost:8080/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": [{"type": "text", "text": "Bob"}], "stream": true}'
```

### Health

```bash
curl http://localhost:8080/liveness
```
