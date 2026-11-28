"""Health. Every API exposes it at the root."""

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app import __version__


@api_view(["GET"])
def health(request) -> Response:
    return Response({"status": "ok", "version": __version__})
