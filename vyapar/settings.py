"""
Django settings for vyapar project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import logging.config
import os
from pathlib import Path

import environ
from django.utils.log import DEFAULT_LOGGING

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    LOGLEVEL=(str, "INFO"),
    DEBUG_SQL=(bool, False),
    ATOMIC_REQUESTS=(bool, True),
    JWT_SECRET_KEY=(
        str,
        "6L,TvCr.pve><r}z>fFR};nM/x!#>2zF=*{B|'&‡9B<B7gjkwkYO}ag/EiGvDm>",
    ),
    JWT_EXPIRY_MINUTES=(int, 10080),
)
env.read_env(os.path.join(BASE_DIR, ".env"))
# Get the SECRETS from environment variables
JWT_SECRET_KEY = env("JWT_SECRET_KEY")
JWT_EXPIRY_MINUTES = env("JWT_EXPIRY_MINUTES")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*s12bdj64p6s(n6b^tabcyd_01j7i^4oa7g^z2t!$k)%frd^%e"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core.apps.CoreConfig",
    "user.apps.UserConfig",
]

MIDDLEWARE = [
    "log_request_id.middleware.RequestIDMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vyapar.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "vyapar.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": env("ATOMIC_REQUESTS"),
    }
}
db_from_env = env.db(default="psql://postgres:postgres@localhost:5432/vyapar")
DATABASES["default"].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Disable Django's logging setup

LOGGING_CONFIG = None
LOGLEVEL = env("LOGLEVEL")


__DJANGO_SERVER_LOGGING_CONFIG = DEFAULT_LOGGING["handlers"]["django.server"]
__DJANGO_SERVER_LOGGING_CONFIG["filters"] = __DJANGO_SERVER_LOGGING_CONFIG.get("filters", [])
__DJANGO_SERVER_LOGGING_CONFIG["filters"].append("request_id")
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"request_id": {"()": "log_request_id.filters.RequestIDFilter"}},
        "formatters": {
            "default": {
                # exact format is not important, this is the minimum information
                "format": "%(asctime)s %(request_id)32s %(levelname).4s %(name)-12s %(message)s"  # noqa: E501
            },
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            # console logs to stderr
            "console": {
                "filters": ["request_id"],
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "django.server": __DJANGO_SERVER_LOGGING_CONFIG,
        },
        "loggers": {
            # default for all undefined Python modules
            "": {"level": LOGLEVEL, "handlers": ["console"]}
        },
    }
)

# django-log-request-id settings
LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"
GENERATE_REQUEST_ID_IF_NOT_IN_HEADER = True
# Send this header in response with request ID
REQUEST_ID_RESPONSE_HEADER = "X_REQUEST_ID"
# Print all requests to logs
LOG_REQUESTS = True


# for printing queries on terminal
if env("DEBUG_SQL"):
    log = logging.getLogger("django.db.backends")
    log.setLevel(logging.DEBUG)


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Rest framework settings
REST_FRAMEWORK_DEFAULT_RENDERER_CLASSES = ("core.renderers.PydanticRenderer",)

if DEBUG:
    REST_FRAMEWORK_DEFAULT_RENDERER_CLASSES = REST_FRAMEWORK_DEFAULT_RENDERER_CLASSES + (
        "rest_framework.renderers.BrowsableAPIRenderer",
    )

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": REST_FRAMEWORK_DEFAULT_RENDERER_CLASSES,
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "EXCEPTION_HANDLER": "core.utils.custom_exception_handler",
}
