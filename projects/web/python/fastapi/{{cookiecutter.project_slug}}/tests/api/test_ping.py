from app import __version__
from tests.support import make_client


def test_ping():
    response = make_client().get("/ping")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": __version__}
