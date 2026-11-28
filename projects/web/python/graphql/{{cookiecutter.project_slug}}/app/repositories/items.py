"""In-memory store standing in for a database or an external API. Replace it; keep the interface."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ItemRow:
    id: int
    name: str


class ItemRepository:
    def __init__(self) -> None:
        self.rows: dict[int, ItemRow] = {}
        self.last_id = 0

    def list(self) -> list[ItemRow]:
        return list(self.rows.values())

    def get(self, id: int) -> ItemRow | None:
        return self.rows.get(id)

    def add(self, name: str) -> ItemRow:
        self.last_id += 1
        item = ItemRow(id=self.last_id, name=name)
        self.rows[item.id] = item

        return item


item_repository = ItemRepository()


def get_item_repository() -> ItemRepository:
    return item_repository
