"""
Django settings for homebooks project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# built-in
import os
from pathlib import Path

# pypi
from dotenv import load_dotenv

# module
from homebooks.settings.base import *

DEV_ENV = REPO_DIR / "servers" / "development" / ".env.development"
if Path(DEV_ENV).exists():
    load_dotenv(DEV_ENV)
else:
    print("ENVFILE NOT LOADED BY LOADENV")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SERVER_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
INTERNAL_IPS = ["127.0.0.1"]  # debug_toolbar

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps, 3rd party
    "debug_toolbar",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_jwt",
    "corsheaders",
    "django_pydenticon",
    "django_extensions",
    "drf_yasg",
    # apps, local
    "accounts",
    "bookshelves",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# username:password@host:port/database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": "postgres",
        "PASSWORD": "example",
        "HOST": "postgres",
        "PORT": "5432",
        "NAME": "postgres",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ),
}

CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
