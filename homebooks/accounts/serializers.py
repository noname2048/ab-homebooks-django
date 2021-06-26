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

    def validate_password1(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("이름은 2글자 이상이어야 합니다.")
        return value

    def validate_password2(self, value):
        pass
        # raise serializers.ValidationError("두 비밀번호가 일치하지 않습니다.")

        return value

    def validate(self, data):
        if data["password1"] and data["password2"] and data["password1"] != data["password2"]:
            raise serializers.ValidationError({"password2": "두 비밀번호가 일치하지 않습니다."})
        return super().validate(data)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password1"))
        validated_data.pop("password1")
        validated_data.pop("password2")
        return User.objects.create(**validated_data)


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
            "name",
            "password1",
            "password2",
        )

    def validate(self, attrs):
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError({"email", ("Email is already in use",)})

        password1 = attrs["password1"]
        password2 = attrs["password2"]

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError({"password2", ("password mismatch",)})

        return super().validate(attrs)

    def create(self, validated_data, commit=True):
        validated_data["password"] = make_password(validated_data.get("password1"))
        validated_data.pop("password1")
        validated_data.pop("password2")
        user = User(**validated_data)
        if commit:
            user.save(commit=commit)

        return user
