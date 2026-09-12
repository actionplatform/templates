"""Health endpoint."""

from fastapi import APIRouter

from app.settings import settings

health_router = APIRouter()


@health_router.get("")
def get_health() -> dict[str, str]:
    return {
        "status": "ok",
        "version": settings.api_version,
        "scope": settings.scope,
    }
