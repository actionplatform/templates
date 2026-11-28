from app.core.errors import NotFoundError, ValidationError
from app.repositories.items import ItemRepository, ItemRow

MAX_NAME = 40


class ItemService:
    def __init__(self, repository: ItemRepository) -> None:
        self.repository = repository

    def list(self) -> list[ItemRow]:
        return self.repository.list()

    def get(self, id: int) -> ItemRow:
        item = self.repository.get(id)

        if item is None:
            raise NotFoundError(f"item {id} not found")

        return item

    def create(self, name: str) -> ItemRow:
        name = name.strip()

        if not name:
            raise ValidationError("name is required", field="name")

        if len(name) > MAX_NAME:
            raise ValidationError(
                f"name is longer than {MAX_NAME} characters", field="name"
            )

        return self.repository.add(name)
