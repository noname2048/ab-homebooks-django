from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_active"]


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        help_text="type backup password",
        style={"input_type": "password", "placeholder": "password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text="type backup password",
        style={"input_type": "password", "placeholder": "password"},
    )

    class Meta:
        model = User
        fields = (
            "email",
            "full_name",
        )

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password1"))
        return super().create(validated_data)


class SignupModelSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        help_text="type backup password",
        style={"input_type": "password", "placeholder": "password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text="type backup password",
        style={"input_type": "password", "placeholder": "password"},
    )

    class Meta:
        model = User
        fields = (
            "email",
            "full_name",
        )

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password1"))
        return super().create(validated_data)
