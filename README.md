# what-i-ate

A Python HTTP service using FastAPI for food-related tracking. The client will be built in Flutter.

## Features

- Health check endpoint (`/health`)
- Agent endpoint (`/agent`) for processing queries
- Built with FastAPI and Pydantic
- Ready for integration with LangChain/LangGraph

## Installation

```bash
pip install -e ".[dev]"
```

## Running the Service

```bash
uvicorn app.main:app --reload
```

The service will be available at `http://localhost:8000`.

## API Documentation

Once the service is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### GET /health
Health check endpoint that returns the service status.

**Response:**
```json
{
  "status": "ok"
}
```

### POST /agent
Agent endpoint that processes queries.

**Request Body:**
```json
{
  "query": "What did I eat for breakfast?"
}
```

**Response:**
```json
{
  "response": "Received query: What did I eat for breakfast?"
}
```

## Development

### Running Tests

```bash
pytest tests/
```

### Linting

```bash
ruff check .
```

## Dependencies

- FastAPI: Web framework
- Pydantic: Data validation
- LangChain: LLM framework (ready for integration)
- LangGraph: Graph-based workflow framework (ready for integration)
