from fastapi.testclient import TestClient

from app import __version__, create_app

client = TestClient(create_app())


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": __version__}


def test_hello():
    response = client.get("/api/v1/hello", params={"name": "ana"})
    assert response.status_code == 200
    assert response.json() == {"message": "hello, ana"}
