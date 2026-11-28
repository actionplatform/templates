from django.urls import include, path

from app.health import health

handler404 = "app.core.errors.not_found"

urlpatterns = [
    path("health", health),
    path("api/v1/", include("app.items.urls")),
]
