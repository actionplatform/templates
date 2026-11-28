from dataclasses import asdict, dataclass

from app.core.errors import ValidationError


@dataclass(frozen=True)
class Item:
    id: int
    name: str

    def as_json(self) -> dict:
        return asdict(self)


def parse_item_create(payload: object) -> str:
    """The name of a valid create request; anything else is a ValidationError."""
    if not isinstance(payload, dict):
        raise ValidationError("body must be a JSON object")

    name = payload.get("name")

    if not isinstance(name, str):
        raise ValidationError("name must be a string", field="name")

    return name
