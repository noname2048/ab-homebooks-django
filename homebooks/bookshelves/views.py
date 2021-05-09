from django.shortcuts import render

from rest_framework.viewsets import ViewSet, ModelViewSet


from bookshelves.models import Bookshelf
from bookshelves.serializers import BookshelfSerializer


class BookshelfViewSet(ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer
