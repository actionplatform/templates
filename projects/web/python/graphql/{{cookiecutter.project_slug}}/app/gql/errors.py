"""Turns a DomainError into a GraphQL error carrying code and field."""

from collections.abc import Iterator
from contextlib import contextmanager

from graphql import GraphQLError

from app.core.errors import DomainError


@contextmanager
def graphql_errors() -> Iterator[None]:
    try:
        yield
    except DomainError as exc:
        raise GraphQLError(
            exc.message,
            extensions={"code": exc.code, "field": exc.field},
        ) from exc
