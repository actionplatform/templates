"""GraphQL types: the contract of every query and mutation."""

import strawberry

from app.repositories.items import ItemRow


@strawberry.type
class Item:
    id: int
    name: str

    @classmethod
    def from_row(cls, row: ItemRow) -> "Item":
        return cls(id=row.id, name=row.name)


@strawberry.input
class ItemInput:
    name: str
