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
from .tasks import request_book_info


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer
    permission_classes = [permissions.AllowAny]

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
        queryset = self.get_queryset()
        name = request.GET.get("q")

        if request.auth:
            queryset = queryset.filter(user=request.auth)

        if name:
            queryset = queryset.filter(name__icontains="name")

        serializer = BookInfoSerializer(queryset, many=True)
        return Response(
            {"data": serializer.data, "name": name}, status=rest_framework.status.HTTP_200_OK
        )


class BookCreateView(generics.CreateAPIView):
    def create(self, request: Request, *args, **kwargs) -> Response:

        isbn = request.POST.get("isbn")
        if len(isbn) != 13:
            return Response(
                {"message": "잘못된 isbn 요청입니다."}, status=rest_framework.status.HTTP_400_BAD_REQUEST
            )
        queryset = Book.objects.filter(isbn=isbn)
        if queryset:
            return Response(
                {"message": "book alreaady exists"},
                status=rest_framework.status.HTTP_400_BAD_REQUEST,
            )
        else:
            data = {"isbn": isbn, "bookshelf": request.user.bookshelf_set.first.id}
            serializer = UserBookRegisterSerializer(data=data)
            serializer.save()

            return Response(serializer.data, status=rest_framework.status.HTTP_201_CREATED)


book_list = BookListView.as_view()
book_create = BookCreateView.as_view()
