from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.shortcuts import resolve_url


class User(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    # objects

    avatar = models.ImageField(
        _("avatar"),
        blank=True,
        upload_to="accounts/profile/%y/%m/%d/%S",
        help_text="1024px 이하의 정사각형 크기의 png/jpg 파일을 업로드 해주세요.",
    )

    GENDER_CHOICES = (
        ("M", "남자"),
        ("F", "여자"),
        ("N", "선택하지 않음"),
    )

    gender = models.CharField(_("gender"), max_length=1, blank=True, choices=GENDER_CHOICES)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)

class NoPasswordUser(AbstractBaseUser):
    name = models.CharField("name", max_length=40)
    email = models.EmailField("email", max_length=120)
    avatar = models.ImageField("avatar",
    blank=True, upload_to="accounts/profile/%y/%m/%d/%S")