"""Builders every test can share, so a change in setup is made once."""

from rest_framework.test import APIClient


def make_client() -> APIClient:
    return APIClient()
