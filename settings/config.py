 # taiga-docker/settings/config.py

# 1. Pull in all the standard Taiga settings
from .common import *  # noqa, pylint: disable=unused-wildcard-import

#########################################
# CORS HEADERS (django-cors-headers)
#########################################

INSTALLED_APPS += [
    "corsheaders",
]

# Must come before CommonMiddleware in settings.common
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]
CORS_ALLOW_HEADERS = [
    "Authorization",
    "Content-Type",
]
