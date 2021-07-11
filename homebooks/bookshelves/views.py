from django.shortcuts import render

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response


from bookshelves.models import Bookshelf
from bookshelves.serializers import BookshelfSerializer


class MyBookshelfViewSet(ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def list(self, request):
        pass

    def create(self, request):
        pass
