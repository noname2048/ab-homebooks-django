from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods

from .forms import AccountEmailForm, AccountSignupForm
from rest_framework.views import APIView

import json
from rest_framework.response import Response
from django.http.response import JsonResponse
import traceback

User = get_user_model()


@require_http_methods(["OPTION", "GET", "POST"])
def discover_existence_from_email(request: HttpRequest):
    """POST 형식의 email params 에서 유저 정보가 있는지 확인한다."""
    if request.method == "OPTION":
        response = HttpResponse()
        response["allow"] = ",".join(["OPTION", "GET", "POST"])
        return HttpResponse()

    if request.method == "GET":
        return render(request, "accounts/empty.html", {"form": AccountEmailForm()})

    if "email" not in request.POST:
        return HttpResponseBadRequest("Email is not included")

    email = request.POST.get("email")

    email_validator = EmailValidator()
    try:
        email_validator(email)
    except ValidationError as e:
        return HttpResponseBadRequest("Email is not valid")

    if User.objects.filter(email=email) != None:
        return HttpResponse("user exists")


def signup_view(request: HttpRequest):
    pass
    # TODO: user will not use password
    if request.method == "POST":

        form = AccountSignupForm(request.POST)
        if form.is_valid():
            signup_user = form.save(commit=False)
            auth_login(signup_user)


from .serializers import SignupSerializer


class SignupAPIView(APIView):
    def get(self, request):
        serializer = SignupSerializer()
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(request.body)
        try:
            if not data["email"]:
                return JsonResponse({"message": "Email required"}, status=400)
        except ValidationError as e:
            tb = traceback.format_exc()
        except KeyError:
            return JsonResponse({"message": "Key_error"}, status=400)


from django.views import generic
from .forms import SignupForm, SignupModelForm
from .serializers import SignupSerializer, SignupModelSerializer

from django.views.decorators.http import require_http_methods
from django.contrib.auth import hashers


class DoneView(generic.TemplateView):
    template_name = "accounts/done.html"


@require_http_methods(["GET", "POST"])
def fbv_form_signup_view(request: HttpRequest):
    if request.method == "GET":
        form = SignupForm()
        return render(
            request,
            "accounts/empty.html",
            {
                "form": form,
            },
        )

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User(
                email=data["email"],
                name=data["name"],
            )
            user.set_password(data["password1"])

            return JsonResponse(
                {
                    "message": "user creation request accepted",
                    "data": {
                        "email": user.email,
                        "name": user.name,
                    },
                },
                status=201,
            )

        return JsonResponse(form.errors, status=400)


def signup_modelform_view(request: HttpRequest):
    if request.method == "GET":
        form = SignupModelForm()
        return render(request, "accounts/signupformview.html", {"form": form})

    if request.method == "POST":
        form = SignupModelForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            data = {
                "message": "done",
                "email": user.email,
                "name": user.name,
            }
            return JsonResponse(data, status=201)
        return JsonResponse(form.errors, status=400)


from django import forms
from django.urls import reverse_lazy


class SignupFormView(generic.FormView):
    template_name = "accounts/signupformview.html"
    form_class: forms.Form = SignupForm
    success_url = reverse_lazy("accounts:done")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        name = form.cleaned_data["name"]
        user = User(
            email=email,
            name=name,
        )
        return super().form_valid(form)


class SignupView(generic.CreateView):
    form_class: forms.ModelForm = SignupModelForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("create_user_done")

    def form_valid(self, form):
        obj = form


from .serializers import SignupSerializer


from logging import getLogger

logger = getLogger(__name__)


from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import (
    api_view,
    renderer_classes,
    authentication_classes,
    permission_classes,
)
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.permissions import AllowAny


@api_view(("GET", "POST"))
# @renderer_classes(
#     (
#         TemplateHTMLRenderer,
#         JSONRenderer,
#     )
# )
#
@permission_classes((AllowAny,))
def signup_serializer_view(request: HttpRequest):
    if request.method == "GET":
        serializer = SignupSerializer()
        return JsonResponse(serializer.data)

    if request.method == "POST":
        serializer = SignupSerializer(data=request.POST)
        if serializer.is_valid():
            return JsonResponse(
                {
                    "message": "done",
                    "email": serializer.validated_data["email"],
                    "name": serializer.validated_data["name"],
                },
                status=201,
            )

        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # (serializer.errors, status=400)


class DjangoCustomSignupClassView(generic.View):
    welcome_message = "welcome"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = DjangoCustomSignupForm()
        data = form.a
        data["message"] = self.welcome_message
        return JsonResponse(form.cleaned_data)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = DjangoCustomSignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data["message"] = self.welcome_message
            return JsonResponse(data)


from django.views import generic


class DjangoCustomSignupCreateView(generic.CreateView):
    pass


from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateListView(APIView):

    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        usernames = [u.email for u in User.objects.all()]
        return Response(usernames)

    def post(self, request, format=None):
        serializer = SignupModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data, commit=False)
            return Response({"email": user.email, "name": user.name})

        ret = {key: value for key, value in serializer.data if key in ("email", "name")}
        ret.update(serializer.errors)
        return Response(ret, status=400)


from .serializers import LoginSerializer


class UserLoginPostView(APIView):

    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User.objects.filter(email=validated_data["email"], name=validated_data["name"])[
                :1
            ]
            if user.exists:
                return Response({"message": "user exist"}, status=200)

            return Response({"messages": "user not exist"}, status=404)
        return Response(
            {"messages": "none validated data", "detail": serializer.errors}, status=400
        )
