from django.urls import path
from django_pydenticon.views import image as pydenticon_image

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from accounts.views import discover_existence_from_email


urlpatterns = [
    path(
        "pydenticon/image/<path:data>.png", pydenticon_image, name="pydenticon_image"
    ),  # pydention
    path("token-auth/", obtain_jwt_token),  # login
    path("token-auth/refresh/", refresh_jwt_token),  # refresh
    path("email", discover_existence_from_email, name="discorver_by_email"),
]
