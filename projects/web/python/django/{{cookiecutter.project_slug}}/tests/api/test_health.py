from django.test import RequestFactory

from app import __version__, create_app
from tests.support import make_client


def test_health():
    response = make_client().get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": __version__}


def test_create_app_builds_a_wsgi_application():
    captured = {}

    def start_response(status, headers):
        captured["status"] = status

    environ = RequestFactory().get("/health").environ

    body = b"".join(create_app()(environ, start_response))

    assert captured["status"].startswith("200")
    assert b'"status"' in body
