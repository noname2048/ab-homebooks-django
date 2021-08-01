from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from . import models

from . import serializers


class BookshelfViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = models.Bookshelf.objects.all()
        queryset = queryset.filter(user=request.user)
        queryset = queryset.order_by("-updated_at")
        serializer = serializers.BookshelfSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.BookshelfSerializer(
            data=request.POST, context={"request", request}
        )
        serializer.save()
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = models.Bookshelf.objects.all()
        queryset = queryset.filter(pk=kwargs["pk"])
        bookshelf = get_object_or_404(queryset)
        return response.Response(bookshelf.values())

    def update(self, request, *args, **kwargs):
        queryset = models.Bookshelf.objects.all()
        queryset = queryset.filter(pk=kwargs["pk"])
        bookshelf = get_object_or_404(queryset)
        serializer = serializers.BookshelfSerializer(
            instance=bookshelf, data=request.POST, context={"request": request}
        )
        serializer.save()
        return serializer

    def destroy(self, request, *args, **kwargs):
        pass

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [permissions.AllowAny]
        elif self.action in ["create", "update", "destroy"]:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
