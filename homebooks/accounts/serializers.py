from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_active"]


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
