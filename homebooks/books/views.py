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


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
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

        serializer = BookSerializer(queryset, many=True)
        return Response(
            {"data": serializer.data, "name": name}, status=rest_framework.status.HTTP_200_OK
        )


class BookCreateView(generics.CreateAPIView):
    def create(self, request):
        # 오로지 ISBN만으로 등록
        isbn = request.POST.get("isbn")
        # TODO: isbn 검색요청을 MSA에 요청. 있을경우 그 정보로 등록

        pass


book_list = BookListView.as_view()
book_create = BookCreateView.as_view()
