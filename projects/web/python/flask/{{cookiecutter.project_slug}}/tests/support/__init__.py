"""Builders every test can share, so a change in setup is made once."""

from flask.testing import FlaskClient

from app import create_app


def make_client() -> FlaskClient:
    return create_app().test_client()
