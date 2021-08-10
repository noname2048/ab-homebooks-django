from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

app_name = "mybooks"

router = DefaultRouter()
router.register("", views.BookshelfViewSet, basename="bookshelf")
router.register("bookshelf/<int:pk>/", views.BookshelfBookViewSet, basename="book")

urlpatterns = [
    path("", include(router.urls)),
]
