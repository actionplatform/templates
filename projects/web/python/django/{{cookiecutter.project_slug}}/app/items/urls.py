from django.urls import path

from app.items.views import ItemDetail, ItemList

urlpatterns = [
    path("items", ItemList.as_view()),
    path("items/<int:id>", ItemDetail.as_view()),
]
