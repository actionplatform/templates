"""WSGI entry point: `gunicorn app.wsgi:application`."""

from app import create_app

application = create_app()
