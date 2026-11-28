"""HTTP only: parse, call the service, serialize. No rules."""

from rest_framework.response import Response
from rest_framework.views import APIView

from app.items.serializers import ItemCreateSerializer, ItemSerializer
from app.items.services import ItemService


class ItemList(APIView):
    service = ItemService()

    def get(self, request) -> Response:
        return Response(ItemSerializer(self.service.list(), many=True).data)

    def post(self, request) -> Response:
        body = ItemCreateSerializer(data=request.data)
        body.is_valid(raise_exception=True)
        item = self.service.create(body.validated_data["name"])

        return Response(ItemSerializer(item).data, status=201)


class ItemDetail(APIView):
    service = ItemService()

    def get(self, request, id: int) -> Response:
        return Response(ItemSerializer(self.service.get(id)).data)
