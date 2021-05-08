from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "avatar_url_image",
        "username",
        "email",
        "is_staff",
        "password",
    ]

    def avatar_url_image(self, obj):
        return mark_safe(f'<img src={obj.avatar_url} "width=30px" height="30px" />')
