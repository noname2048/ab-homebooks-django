from django.views.generic import TemplateView

from django.http.request import HttpRequest
from django.http.response import HttpResponse


class Home(TemplateView):
    template_name = "home.html"
