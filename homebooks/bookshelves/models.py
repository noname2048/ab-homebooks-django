from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

user_model = get_user_model()


class Bookshelf(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        user_model,
        on_delete=models.deletion.PROTECT,
        blank=True,
    )

    name = models.CharField(
        _("name"),
        max_length=100,
        blank=True,
    )

    address = models.CharField(
        _("address"),
        max_length=200,
        blank=True,
    )
