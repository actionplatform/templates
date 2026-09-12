"""{{ cookiecutter.project_name }} — FastAPI application factory."""

__version__ = "0.1.0"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.ping import ping_router
from app.api.v1 import api_router as v1_router
from app.settings import settings


def create_app() -> FastAPI:
    """Create the FastAPI application."""
    docs_url = "/docs" if settings.is_development else None
    openapi_url = "/openapi.json" if settings.is_development else None

    new_app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        description="{{ cookiecutter.description }}",
        version=settings.api_version,
        debug=settings.is_development,
        docs_url=docs_url,
        openapi_url=openapi_url,
    )

    new_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )

    new_app.include_router(ping_router, prefix="/ping")
    new_app.include_router(v1_router, prefix=settings.api_v1_prefix)

    return new_app


app = create_app()
