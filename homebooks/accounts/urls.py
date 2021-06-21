from django.urls import path
from django_pydenticon.views import image as pydenticon_image

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import discover_existence_from_email
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path("pydenticon/<path:data>.png", pydenticon_image, name="pydenticon"),  # pydention
    # path("token-auth/", obtain_jwt_token),  # login
    # path("token-auth/refresh/", refresh_jwt_token),  # refresh
    path("email", discover_existence_from_email, name="discorver_by_email"),
    path("api/token/", TokenRefreshView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # signup forms
    path("signup/done/", TemplateView(template_name="accounts/done.html").as_view(), name="done"),
    path("signup/fbv/", fbv_form_signup_view, name="fbv"),
    path("signup/formview/", SignupFormView.as_view(), name="cbvFormView"),
    path("signup/modelform/", fbv_form_signup_view),
    path("signup/createview/", DjangoCustomSignupClassView.as_view(), name="cbv_base"),
    path("signup/modelform/", DjangoCustomSignupCreateView.as_view(), name="cbv_create"),
    # path("signup/serializer/"),
    # path("signup/modelserializer/"),
    # TODO: drf
    # path("drf/signup/", ),
]
