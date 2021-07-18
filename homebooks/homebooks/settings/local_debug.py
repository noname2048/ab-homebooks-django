import os
from pathlib import Path
from dotenv import load_dotenv
from homebooks.settings.base import *
from datetime import timedelta

ENV_FILE_DIR: Path = REPO_DIR / "envs" / "local_debug.env"
SECRET_FILE_DIR: Path = REPO_DIR / "envs" / "secret.env"

if ENV_FILE_DIR.exists() and ENV_FILE_DIR.is_file():
    load_dotenv(ENV_FILE_DIR)
    load_dotenv(SECRET_FILE_DIR)

DEBUG = True
SECRET_KEY = os.environ["SERVER_SECRET_KEY"]

ALLOWED_HOSTS = []
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]  # from corsheaders
INTERNAL_IPS = ["127.0.0.1"]  # from debug_toolbar

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
    # "rest_framework.authtoken",
    # "rest_framework_jwt",
    "corsheaders",
    "django_pydenticon",
    "django_extensions",
    "drf_yasg",
    "django_celery_results",
    # apps, local
    "accounts",
    "bookshelves",
    "books",
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

# username:password@host:port/database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": "postgres",
        "PASSWORD": "example",
        "HOST": "localhost",
        "PORT": "9001",
        "NAME": "postgres",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

AUTHENTICATION_BACKENDS = [
    "accounts.my_auth.MyBackend",  # 우리가 만든 AUTH를 먼저 검사
    "django.contrib.auth.backends.ModelBackend",  # Django가 관리하는 AUTH
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "homebooks": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]

CELERY_TIMEZONE = "Asia/Seoul"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_RESULT_BACKEND = "django-db"
# CELERY_CACHE_BACKEND = "default"
#
# CACHES = {
#     "defualt": {
#         "BACKEND": "django.core.cache.backends.db.DatabaseCache",
#         "LOCATION": "my_cache_table",
#     }
# }

LANGUAGE_CODE = "en-us"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://cfb9333e6e7e4b5ab47d9bb3af458d10@o922767.ingest.sentry.io/5869830",
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
