from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe
from django.template.defaultfilters import truncatechars

from bookshelves.models import Bookshelf

User = get_user_model()


@admin.register(User)
class NopasswordAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "name",
    ]


# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "avatar_url_image",
        "username",
        "email",
        "is_staff",
        "short_password",
        "have_bookshelf",
    ]

    actions = ["make_bookshelf"]

    def short_password(self, obj):
        return truncatechars(obj.password, 10)

    def avatar_url_image(self, obj):
        return mark_safe(f'<img src={obj.avatar_url} "width=30px" height="30px" />')

    def have_bookshelf(self, obj):
        return obj.bookshelf_set.exists()

    @admin.action(description="Make BookShelf, if have not.")
    def make_bookshelf(modelamin, request, queryset):
        users = queryset.all()
        for user in users:
            if user.bookshelf_set.exists() == False:
                user.bookshelf_set.create(name="default")
