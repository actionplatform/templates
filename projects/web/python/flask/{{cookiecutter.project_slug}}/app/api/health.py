"""Health. Every API exposes it at the root."""

from flask import Blueprint, jsonify

health_blueprint = Blueprint("health", __name__)


@health_blueprint.get("/health")
def health():
    from app import __version__

    return jsonify(status="ok", version=__version__)
