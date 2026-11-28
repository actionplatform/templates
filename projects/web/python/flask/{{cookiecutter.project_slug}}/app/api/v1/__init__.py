"""API v1: aggregate every v1 blueprint here."""

from flask import Blueprint

from app.api.v1.items import items_blueprint

v1_blueprint = Blueprint("v1", __name__)
v1_blueprint.register_blueprint(items_blueprint, url_prefix="/items")
