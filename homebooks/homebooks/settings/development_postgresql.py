import os

# username:password@host:port/database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": os.environ["SERVER_DEFAULT_DB_USERNAME"],
        "PASSWORD": os.environ["SERVER_DEFAULT_DB_PASSWORD"],
        "HOST": os.environ["SERVER_DEFAULT_DB_HOST"],
        "PORT": os.environ["SERVER_DEFAULT_DB_PORT"],
        "NAME": os.environ["SERVER_DEFAULT_DB_DBNAME"],
    }
}
