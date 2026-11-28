"""Example resource showing the layers: blueprint → service → repository."""

from flask import Blueprint, current_app, jsonify, request

from app.schemas.items import parse_item_create
from app.services.items import ItemService

items_blueprint = Blueprint("items", __name__)


def service() -> ItemService:
    return current_app.extensions["item_service"]


@items_blueprint.get("")
def list_items():
    return jsonify([item.as_json() for item in service().list()])


@items_blueprint.post("")
def create_item():
    name = parse_item_create(request.get_json(silent=True))

    return jsonify(service().create(name).as_json()), 201


@items_blueprint.get("/<int:id>")
def get_item(id: int):
    return jsonify(service().get(id).as_json())
