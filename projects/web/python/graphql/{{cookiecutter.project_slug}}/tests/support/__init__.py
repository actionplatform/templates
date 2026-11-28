"""Builders every test can share, so a change in setup is made once."""

from fastapi.testclient import TestClient

from app import create_app


def make_client() -> TestClient:
    return TestClient(create_app())


def graphql(client: TestClient, query: str, variables: dict | None = None):
    response = client.post(
        "/graphql", json={"query": query, "variables": variables or {}}
    )

    assert response.status_code == 200

    return response.json()
