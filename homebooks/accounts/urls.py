from django.urls import path
from django_pydenticon.views import image as pydenticon_image

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import discover_existence_from_email
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # pydenticon (profile: avatar)
    path("pydenticon/<path:data>.png", pydenticon_image, name="pydenticon"),
    # is email exists?
    path("email", discover_existence_from_email, name="email_verification"),
    # tokens
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # signup forms
    path("signup/done/", DoneView.as_view(), name="done"),
    path("signup/fbv/", fbv_form_signup_view, name="signup_view"),
    path("signup/formview/", SignupFormView.as_view(), name="signup_formview"),
    path("signup/modelform/", signup_modelform_view, name="signup_modelform_view"),
    path("signup/serializer/", signup_serializer_view, name="signup_serializer_view"),
    path("signup/createview/", DjangoCustomSignupClassView.as_view(), name="cbv_base"),
    path("signup/modelform/", DjangoCustomSignupCreateView.as_view(), name="cbv_create"),
    path("signup/modelserializer/", UserCreateListView.as_view(), name="apiview"),
    path("login/modelserializer/", UserLoginPostView.as_view(), name="loginview"),
]
