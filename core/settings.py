
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import dj_database_url
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rc4x=v+g%ujjdt=^pxq79(_5^p_^g%vv9j0wi@to&+kd--t$7x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['localhost','192.168.56.1','127.0.0.1']
# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = ["usingrender-x7yq.onrender.com", "localhost", "127.0.0.1", "seals-front-end-wh1f.vercel.app"]

# Application definition
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'seals',

]


# For production (recommended)
# In settings.py - ONLY FOR TESTING
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = ['*']

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
]

STATIC_ROOT=BASE_DIR/'staticfiles'
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

import os
import dj_database_url  # optional, simplifies parsing
# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases




# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent



# Copy the "External Database URL" from your Render Dashboard
# import dj_database_url
# import os

# # MAKE SURE this string includes '.oregon-postgres.render.com' (or similar)
# EXTERNAL_URL = "postgresql://database_k4pc_user:bWp6VRHaxKKYCwLAAT6OfShw8gQliXQg@dpg-d67m5cc9c44c73dn06q0-a.singapore-postgres.render.com/database_k4pc"

# DATABASES = {
#     'default': dj_database_url.config(
#         default=EXTERNAL_URL,
#         conn_max_age=600,
#         ssl_require=True
#     )
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

import os
import dj_database_url




DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'database_k4pc',
#         'USER': 'database_k4pc_user',
#         'PASSWORD': 'bWp6VRHaxKKYCwLAAT6OfShw8gQliXQg',
#         'HOST': 'dpg-d67m5cc9c44c73dn06q0-a.singapore-postgres.render.com',
#         'PORT': '5432',
#         'OPTIONS': {
#             'sslmode': 'require',
#         },
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
