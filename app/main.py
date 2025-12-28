"""Main FastAPI application for What I Ate service."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="What I Ate", version="0.1.0")


class QueryInput(BaseModel):
    """Input model for agent queries."""

    query: str


class QueryOutput(BaseModel):
    """Output model for agent responses."""

    response: str


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/agent")
async def agent(query_input: QueryInput) -> QueryOutput:
    """Agent endpoint that processes queries.
    
    Args:
        query_input: The query input containing the user's query
        
    Returns:
        QueryOutput: The agent's response
    """
    # Stub implementation - will be enhanced with langchain/langgraph later
    return QueryOutput(response=f"Received query: {query_input.query}")
