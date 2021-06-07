from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods

from .forms import AccountEmailForm, AccountSignupForm

User = get_user_model()


@require_http_methods(["OPTION", "GET", "POST"])
def discover_existence_from_email(request: HttpRequest):
    """POST 형식의 email params 에서 유저 정보가 있는지 확인한다.
    """
    if request.method == "OPTION":
        response = HttpResponse()
        response["allow"] = ','.join(["OPTION", "GET", "POST"])
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
