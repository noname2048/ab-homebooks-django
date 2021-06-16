from django.urls import path
from django_pydenticon.views import image as pydenticon_image

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import discover_existence_from_email


urlpatterns = [
    path("pydenticon/<path:data>.png", pydenticon_image, name="pydenticon"),  # pydention
    # path("token-auth/", obtain_jwt_token),  # login
    # path("token-auth/refresh/", refresh_jwt_token),  # refresh
    path("email", discover_existence_from_email, name="discorver_by_email"),
    path("api/token/", TokenRefreshView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
