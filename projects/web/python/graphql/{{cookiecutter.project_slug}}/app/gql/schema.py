import strawberry

from app.gql.errors import graphql_errors
from app.gql.types import Item, ItemInput
from app.repositories.items import get_item_repository
from app.services.items import ItemService


def service() -> ItemService:
    return ItemService(get_item_repository())


@strawberry.type
class Query:
    @strawberry.field
    def items(self) -> list[Item]:
        return [Item.from_row(row) for row in service().list()]

    @strawberry.field
    def item(self, id: int) -> Item:
        with graphql_errors():
            return Item.from_row(service().get(id))


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, input: ItemInput) -> Item:
        with graphql_errors():
            return Item.from_row(service().create(input.name))


schema = strawberry.Schema(query=Query, mutation=Mutation)
