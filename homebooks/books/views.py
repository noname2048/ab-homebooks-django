import rest_framework.status
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.request import Request
from .models import *
from .serializers import *
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BookViewSet(viewsets.ViewSet):
    """책을 검색하는 API

    - 기본적으로 모든책을 검색합니다.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    @swagger_auto_schema(
        # operation_description="책검색 api",
        responses={
            200: openapi.Response(description="책검색", schema=BookSerializer(many=True)),
            404: "book not found",
        },
    )
    def list(self, request):
        """책검색 API

        - 기본
        """
        name = request.GET.get("q")
        queryset = Book.objects.filter(name__icontains="name")
        serializer = BookSerializer(queryset, many=True)
        return Response(
            {"data": serializer.data, "name": name}, status=rest_framework.status.HTTP_200_OK
        )

    def create(self, request: rest_framework.request.Request) -> rest_framework.response.Response:
        book = BookSerializer(data=request.POST)
        book.save()
        return Response({"data": book}, status=rest_framework.status.HTTP_201_CREATED)


book_list = BookViewSet.as_view({"get": "list"})
book_create = BookViewSet.as_view({"post": "create"})
