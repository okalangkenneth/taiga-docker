# settings/config.py

# 1) Import all of Taiga’s stock settings
from .common import *  # noqa

import os

# 2) Override secret-key & site domain from env
#    (these correspond to the TAIGA_SECRET_KEY, TAIGA_SITES_DOMAIN, TAIGA_SITES_SCHEME vars)
SECRET_KEY = os.environ.get("TAIGA_SECRET_KEY", SECRET_KEY)

SITES["api"]["domain"] = os.environ.get("TAIGA_SITES_DOMAIN", SITES["api"]["domain"])
SITES["api"]["scheme"] = os.environ.get("TAIGA_SITES_SCHEME", SITES["api"]["scheme"])

# 3) Control whether public self-registration is enabled
PUBLIC_REGISTER_ENABLED = os.environ.get("PUBLIC_REGISTER_ENABLED", "False") == "True"


# ──────────────────────────────────────────────────────────────────────────────
# 4) django-cors-headers configuration (make sure you pip-install django-cors-headers
#    into your taiga-back image!)
# ──────────────────────────────────────────────────────────────────────────────

# 4a) Add corsheaders to INSTALLED_APPS
INSTALLED_APPS += [
    "corsheaders",
]

# 4b) Insert its middleware at the very top so it can handle the preflight
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

# 4c) Whitelist your frontend origin(s)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # add your deployed React URL here if different, e.g.
    # "https://my-taiga-frontend.example.com",
]

# 4d) Allow the methods your app will use
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

# 4e) Allow the headers your frontend will send
CORS_ALLOW_HEADERS = [
    "Authorization",
    "Content-Type",
    "X-Requested-With",
]

# 4f) If you need to send cookies or HTTP-auth on cross-site requests
CORS_ALLOW_CREDENTIALS = True

