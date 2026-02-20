# Minimal Invoke Agent

The simplest possible agent — a raw `invoke()` function with zero framework dependencies.

## Run

```bash
pip install azure-ai-agentserver-core
python main.py
```

The server starts on `http://0.0.0.0:8080`.

## Test

### Non-streaming

```bash
curl -s -X POST http://localhost:8080/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": [{"type": "text", "text": "Hello world"}]}'
```

Expected response:

```json
{"status": "completed", "message": "Echo: Hello world", "annotations": []}
```

### Streaming

```bash
curl -s -N -X POST http://localhost:8080/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": [{"type": "text", "text": "Hello world"}], "stream": true}'
```

Expected SSE events:

```
event: message.delta
data: {"type": "message.delta", "delta": "Echo: "}

event: message.delta
data: {"type": "message.delta", "delta": "Hello "}

event: message.delta
data: {"type": "message.delta", "delta": "world"}

event: invocation.completed
data: {"type": "invocation.completed", "status": "completed", "message": "Echo: Hello world", "annotations": []}

data: [DONE]
```

### Health

```bash
curl http://localhost:8080/liveness
curl http://localhost:8080/readiness
```
