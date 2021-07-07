from django.urls import path
from .views import *

app_name = "book"

urlpatterns = [
    path("search/", book_list, name="book_search"),
]
