from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookshelves import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "bookshelves"

router = DefaultRouter()
router.register(r"bookshelves", views.MyBookshelfViewSet)

urlpatterns = [
    *router.urls,
]
