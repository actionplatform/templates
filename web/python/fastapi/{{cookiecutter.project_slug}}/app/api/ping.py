"""Ping. Every API exposes it at the root."""

from fastapi import APIRouter

ping_router = APIRouter(tags=["Ping"])


@ping_router.get("/ping")
def ping() -> dict[str, str]:
    from app import __version__

    return {"status": "ok", "version": __version__}
