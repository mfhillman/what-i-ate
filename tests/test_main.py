"""Tests for the main FastAPI application."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_agent_endpoint():
    """Test the agent endpoint with a query."""
    query_input = {"query": "What did I eat yesterday?"}
    response = client.post("/agent", json=query_input)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert data["response"] == "Received query: What did I eat yesterday?"


def test_agent_endpoint_validation():
    """Test the agent endpoint input validation."""
    # Missing required field
    response = client.post("/agent", json={})
    assert response.status_code == 422


def test_agent_endpoint_with_empty_query():
    """Test the agent endpoint with an empty query."""
    query_input = {"query": ""}
    response = client.post("/agent", json=query_input)
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == "Received query: "
