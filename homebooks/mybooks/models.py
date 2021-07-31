from django.db import models
from django.conf import settings

from homebooks.models import TimeStampedModel


class Bookshelf(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.deletion.CASCADE)
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=10)


class Book(TimeStampedModel):
    bookshelf = models.ForeignKey("Bookshelf", on_delete=models.deletion.CASCADE)
    isbn = models.BigAutoField()
    origin = models.ForeignKey("OriginalBook", on_delete=models.deletion.CASCADE, null=True)
    have = models.BooleanField(blank=True, default=False)


class OriginalBook(TimeStampedModel):
    isbn = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()

    publisher = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
