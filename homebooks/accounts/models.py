import binascii
import os

from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.shortcuts import resolve_url
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.timezone import datetime
from datetime import timedelta


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
        ("N", "표기를 원하지 않음"),
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


class UserManager(BaseUserManager):

    user_in_migrations = True

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email=email, name=name, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user


class NoPasswordUser(AbstractBaseUser):
    """Login by email(send from server) User.

    Email (required)
    name (not required. just name)
    """

    objects = UserManager()

    # base information
    email = models.EmailField(
        "email",
        unique=True,
        max_length=120,
        help_text=_("Required. 120 characters or fewer."),
        error_messages={"unique": _("A user with that username already exists.")},
    )
    name = models.CharField("name", max_length=40)
    address = models.CharField("address", max_length=120, blank=True)

    # site information
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(
        _("activate"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    last_token = models.ForeignKey(
        "accounts.EmailTokenAccess", null=True, on_delete=models.deletion.SET_NULL
    )

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
    ]

    class Meta:
        verbose_name = _("nopassworduser")
        verbose_name_plural = _("nopasswordusers")
        ordering = ("-date_joined",)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.deletion.CASCADE,
        primary_key=True,
    )
    avatar = models.ImageField(
        "avatar",
        blank=True,
        upload_to="accounts/nopassworduser/avatar/%y/%m/%d/%S",
    )

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon", self.user.email)


class EmailTokenAccess(models.Model):
    objects = models.Manager
    token = models.CharField(
        _("key"),
        max_length=40,
        primary_key=True,
    )
    user = models.ForeignKey(
        get_user_model(),
        related_name="email_token",
        on_delete=models.deletion.CASCADE,
        null=True,
    )
    created_at = models.DateTimeField(default=lambda: datetime.now())
    expired_at = models.DateTimeField(default=lambda: datetime.now() + timedelta(days=1))

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
        if not self.expired_at:
            self.expired_at = self.created_at + timedelta(days=1)
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.token

    class Meta:
        ordering = ["-created_at"]
