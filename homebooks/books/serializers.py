from rest_framework import serializers
from .models import Book


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "publisher", "isbn"]


class UserBookRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["bookshelves", "isbn"]
