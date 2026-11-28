"""Domain errors: services raise them, the API answers one JSON shape."""

from django.http import JsonResponse
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import exception_handler

NON_FIELD = "non_field_errors"


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


def first_message(value) -> str:
    while isinstance(value, list | tuple):
        value = value[0] if value else ""

    return str(value)


def validation_detail(detail) -> dict:
    if isinstance(detail, dict) and detail:
        field, messages = next(iter(detail.items()))
        error = {"code": "invalid", "message": first_message(messages)}

        if field != NON_FIELD:
            error["field"] = str(field)

        return error

    return {"code": "invalid", "message": first_message(detail)}


def handle_exception(exc, context):
    """DRF exception handler: every error leaves as {"detail": {code, message, field}}."""
    if isinstance(exc, DomainError):
        return Response({"detail": exc.as_detail()}, status=exc.status_code)

    response = exception_handler(exc, context)

    if response is None:
        return None

    if isinstance(exc, exceptions.ValidationError):
        response.status_code = 422
        response.data = {"detail": validation_detail(exc.detail)}

        return response

    message = response.data.get("detail", "")
    response.data = {
        "detail": {
            "code": getattr(message, "code", "error"),
            "message": str(message),
        }
    }

    return response


def not_found(request, exception=None) -> JsonResponse:
    """Django's 404 for URLs that match no route."""
    return JsonResponse(
        {"detail": {"code": "not_found", "message": "not found"}}, status=404
    )
