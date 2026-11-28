"""Settings, read from the environment: DEBUG, SECRET_KEY and ALLOWED_HOSTS."""

import os
import secrets

DEBUG = os.environ.get("DEBUG", "false").lower() in {"1", "true", "yes"}
SECRET_KEY = os.environ.get("SECRET_KEY") or secrets.token_urlsafe(50)
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("ALLOWED_HOSTS", "*").split(",")
    if host.strip()
]

INSTALLED_APPS = ["rest_framework"]
MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"
DATABASES = {}
USE_TZ = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "EXCEPTION_HANDLER": "app.core.errors.handle_exception",
    "UNAUTHENTICATED_USER": None,
}
