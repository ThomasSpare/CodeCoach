"""
Django settings for chatrooms project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os

import dj_database_url

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [(
#         'rest_framework.authentication.SessionAuthentication'
#         if 'DEV' in os.environ
#         else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
#     )]
# }

# REST_USE_JWT = True
# JWT_AUTH_SECURE = True
# JWT_AUTH_COOKIE = 'my-app-auth'
# JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
# JWT_AUTH_SAMESITE = 'None'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'chatrooms.serializers.CurrentUserSerializer'
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
#DEBUG = 'DEV' in os.environ


# DEBUG = 'DEV' in os.environ

ALLOWED_HOSTS = [
    'localhost',
    '3000-thomasspare-codecoachfr-xylbmbx08l5.ws-eu102.gitpod.io',
    # frontend
    'codecoach-frontend-2102ce726626.herokuapp.com',
    'localhost:3000',
    '127.0.0.1:3000',
    # backend
    'codecoach-a2f14f649917.herokuapp.com',
    '8000-thomasspare-codecoach-spvitnctgqr.ws-eu102.gitpod.io',
    'localhost:8000',
    '127.0.0.1:8000',
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    # frontend
    'https://codecoach-frontend-2102ce726626.herokuapp.com',
    'https://3000-thomasspare-codecoachfr-xylbmbx08l5.ws-eu102.gitpod.io',
    'http://localhost:3000',
    # backend
    'https://codecoach-a2f14f649917.herokuapp.com',
    'https://8000-thomasspare-codecoach-spvitnctgqr.ws-eu102.gitpod.io',
    'http://localhost:8000',
]

CORS_ORIGIN_WHITELIST = [
    # frontend
    'https://3000-thomasspare-codecoachfr-xylbmbx08l5.ws-eu102.gitpod.io',
    'https://codecoach-frontend-2102ce726626.herokuapp.com',
    # backend
    'https://codecoach-a2f14f649917.herokuapp.com',
    'https://8000-thomasspare-codecoach-spvitnctgqr.ws-eu102.gitpod.io',
]

# Application definition

INSTALLED_APPS = [
    # 'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    "corsheaders",
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    # "channels",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    # 'redis',
    'chatapp',
    'profiles',
]

SITE_ID = 1

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

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]

CORS_ALLOW_METHODS: ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
CORS_ALLOW_HEADERS = ["accept", "accept-encoding", "authorization", "content-type", "dnt", "origin", "user-agent", "x-csrftoken", "x-requested-with", ]


CORS_ALLOW_CREDENTIALS = True


ROOT_URLCONF = 'chatrooms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "authentication.exceptions.status_code_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

WSGI_APPLICATION = 'chatrooms.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# set username field to email
AUTH_USER_MODEL_USERNAME_FIELD = "email"


# CHANNEL_LAYERS = {
#         'default': {
#             'BACKEND': 'channels_redis.core.RedisChannelLayer',
#             'CONFIG': {
#                 "hosts": [('127.0.0.1', 6379)],
#             },
#         },
#    }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
#             "capacity": 8000,
#             "channel_capacity": {
#                 "http.request": 8000,
#                 "http.response": 8000,
#                 "http.websocket": 8000,
#                 "websocket.receive": 8000,
#                 "websocket.send": 8000,
#                 "websocket.disconnect": 8000,
#                 "websocket.connect": 8000,
#                 },
#             },
#         },
#     }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True  # added this one one from moments settings

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFTETIME': timedelta(minutes=30),
}

AUTH_USER_MODEL = "profiles.UserAccount"
