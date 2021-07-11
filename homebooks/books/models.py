from django.db import models
from django.utils.translation import gettext_lazy as _

from bookshelves.models import Bookshelf


class Book(models.Model):

    objects = models.Manager
    name = models.CharField(
        _("name"),
        max_length=100,
    )

    long_name = models.CharField(
        _("long_name"),
        max_length=200,
    )

    isbn = models.SlugField(
        _("isbn"),
        max_length=50,
        allow_unicode=False,
    )

    bookshelf = models.ForeignKey(
        Bookshelf,
        on_delete=models.deletion.CASCADE,
    )
