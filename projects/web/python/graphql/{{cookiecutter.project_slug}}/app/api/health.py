"""Health. Every API exposes it at the root."""

from fastapi import APIRouter

health_router = APIRouter(tags=["Health"])


@health_router.get("/health")
def health() -> dict[str, str]:
    from app import __version__

    return {"status": "ok", "version": __version__}
