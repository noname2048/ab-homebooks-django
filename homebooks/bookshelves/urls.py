from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookshelves import views

router = DefaultRouter()
router.register("bookshelves", views.BookshelfViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
