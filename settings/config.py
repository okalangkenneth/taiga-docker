# settings/config.py
from .common import *  # noqa

# Enable django-cors-headers
INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

# CORS rules
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
CORS_ALLOW_METHODS = ["GET","POST","PUT","PATCH","DELETE","OPTIONS"]
CORS_ALLOW_HEADERS = ["Authorization","Content-Type"]

