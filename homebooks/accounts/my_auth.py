from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

UserModel = get_user_model()


class MyBackend(BaseBackend):
    def authenticate(self, email, token=None):
        try:
            user = UserModel.objects.get(email=email)
            return user
        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
