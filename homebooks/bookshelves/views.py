import rest_framework.status
from django.shortcuts import render

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request


from bookshelves.models import Bookshelf
from bookshelves.serializers import BookshelfSerializer
from .forms import BookshelfForm
from accounts.serializers import UserSerializer

import logging

logger = logging.getLogger("bookshelves")


class MyBookshelfViewSet(ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def get_queryset(self):
        return self.request.user.bookshelf_set.all()

    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = BookshelfSerializer(queryset, many=True)
        return Response(serializer.data, status=rest_framework.status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs) -> Response:
        data = {"user": request.user.id, "name": request.POST.get("name")}
        serializer = BookshelfSerializer(data=data)

        logger.warning("warning")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            ret = serializer.errors
            ret["data"] = serializer.data
            return Response(ret)
