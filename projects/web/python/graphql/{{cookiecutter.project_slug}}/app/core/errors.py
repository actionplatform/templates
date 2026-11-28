"""Domain errors: services raise them, the GraphQL layer translates them."""


class DomainError(Exception):
    code = "domain_error"

    def __init__(self, message: str, field: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.field = field


class NotFoundError(DomainError):
    code = "not_found"


class ValidationError(DomainError):
    code = "invalid"


class ConflictError(DomainError):
    code = "conflict"
