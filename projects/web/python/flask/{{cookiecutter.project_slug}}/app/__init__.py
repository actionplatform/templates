"""{{ cookiecutter.project_name }} — Flask application factory."""

__version__ = "0.0.0"

from flask import Flask

from app.api.health import health_blueprint
from app.api.v1 import v1_blueprint
from app.core.errors import install_error_handlers
from app.repositories.items import ItemRepository
from app.services.items import ItemService

API_V1_PREFIX = "/api/v1"


def create_app() -> Flask:
    """Create the Flask application."""
    new_app = Flask(__name__)
    new_app.extensions["item_service"] = ItemService(ItemRepository())

    install_error_handlers(new_app)
    new_app.register_blueprint(health_blueprint)
    new_app.register_blueprint(v1_blueprint, url_prefix=API_V1_PREFIX)

    return new_app
