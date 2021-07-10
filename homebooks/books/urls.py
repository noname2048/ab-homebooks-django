from django.urls import path
from .views import *

app_name = "book"

urlpatterns = [
    path("search/", book_list, name="book_search"),
    path("create/", book_create, name="book_create"),
]
