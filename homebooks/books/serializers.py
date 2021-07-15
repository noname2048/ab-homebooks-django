from rest_framework import serializers
from .models import Book


class UserBookRegister(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["bookshelves", "isbn"]
