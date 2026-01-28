import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS=[os.environ.get['RENDER_EXTERNAL_HOSTNAME']]
CSRG_TRUSTED_ORIGINS=['https://'+os.environ.get['RENDER_EXTERNAL_HOSTNAME']]
DEBUG=False
SECRET_KEY=os.environ.gte['SECRET_KEY']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOW_ALL_ORIGINS = True # Allow your React dev server to talk to Django
# CORS_ALLOWED_ORIGINS=['http://localhost:8081']

STORAGES={
    "default":{
        "BACKEND":"django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedStaticFilesStorage"
    },
}
DATABASES={
    'default':dj_database_url.config(
default=os.environ['DATABASE_URL'],
conn_max_age=600
    )
}

