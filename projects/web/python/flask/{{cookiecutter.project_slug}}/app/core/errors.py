"""Domain errors: services raise them, the app translates them to one JSON shape."""

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException


class DomainError(Exception):
    status_code = 400
    code = "domain_error"

    def __init__(self, message: str, field: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.field = field

    def as_detail(self) -> dict:
        detail = {"code": self.code, "message": self.message}

        if self.field is not None:
            detail["field"] = self.field

        return detail


class NotFoundError(DomainError):
    status_code = 404
    code = "not_found"


class ValidationError(DomainError):
    status_code = 422
    code = "invalid"


class ConflictError(DomainError):
    status_code = 409
    code = "conflict"


def install_error_handlers(app: Flask) -> None:
    @app.errorhandler(DomainError)
    def domain_error(exc: DomainError):
        return jsonify(detail=exc.as_detail()), exc.status_code

    @app.errorhandler(HTTPException)
    def http_error(exc: HTTPException):
        code = (exc.name or "error").lower().replace(" ", "_")
        detail = {"code": code, "message": exc.description or exc.name}

        return jsonify(detail=detail), exc.code or 500
