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
from .forms import DjangoCustomSignupForm

from django.views.decorators.http import require_http_methods
from django.contrib.auth import hashers


@require_http_methods(["GET", "POST"])
def django_custom_signup_function_view(request: HttpRequest):
    if request.method == "GET":
        form = DjangoCustomSignupForm()
        return render(
            request,
            "accounts/empty.html",
            {
                "form": form,
            },
        )

    if request.method == "POST":
        form = DjangoCustomSignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User(
                email=data["email"],
                name=data["name"],
            )
            user.set_password(data["password"])
            user.save(commit=True)

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
