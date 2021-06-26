import os
from pathlib import Path
from dotenv import load_dotenv
from homebooks.settings.base import *


ENV_FILE_DIR: Path = REPO_DIR / "envs" / "local_debug.env"
if ENV_FILE_DIR.exists() and ENV_FILE_DIR.is_file():
    load_dotenv(ENV_FILE_DIR)

DEBUG = True
SECRET_KEY = os.environ["SERVER_SECRET_KEY"]

ALLOWED_HOSTS = []
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]  # from corsheaders
INTERNAL_IPS = ["127.0.0.1"]  # from debug_toolbar

INSTALLED_APPS = []
