"""{{ cookiecutter.project_name }} — Django application factory."""

import os

__version__ = "0.0.0"


def create_app():
    """Create the WSGI application."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    from django.core.wsgi import get_wsgi_application

    return get_wsgi_application()
