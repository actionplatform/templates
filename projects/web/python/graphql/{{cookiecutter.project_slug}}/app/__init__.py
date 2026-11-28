"""{{ cookiecutter.project_name }} — Strawberry GraphQL on FastAPI."""

__version__ = "0.0.0"

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.api.health import health_router
from app.gql import schema


def create_app() -> FastAPI:
    """Create the FastAPI application."""
    new_app = FastAPI(
        title="{{ cookiecutter.project_name }}",
        description="{{ cookiecutter.description }}",
        version=__version__,
    )

    new_app.include_router(health_router)
    new_app.include_router(GraphQLRouter(schema), prefix="/graphql")

    return new_app


app = create_app()
