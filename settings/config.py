# settings/config.py
# 1) import all the stock Taiga settings
from .common import *  # noqa

# 2) enable django-cors-headers
INSTALLED_APPS += [
    "corsheaders",
]

# must come before CommonMiddleware
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

# 3) CORS settings
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

