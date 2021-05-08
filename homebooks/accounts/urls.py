from django.urls import path
from django_pydenticon.views import image as pydenticon_image


urlpatterns = [
    path("pydenticon/image/<path:data>.png", pydenticon_image, name="pydenticon_image"),
]
