from django.contrib import admin
from .models import Bookshelf


@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "user",
    )
    list_display = (
        "name",
        "user",
    )
