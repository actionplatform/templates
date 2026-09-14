"""Ping. Every API exposes it at the root."""

from fastapi import APIRouter

from app.schemas.health import Health

ping_router = APIRouter(tags=["Ping"])


@ping_router.get("/ping")
def ping() -> Health:
    from app import __version__

    return Health(status="ok", version=__version__)
