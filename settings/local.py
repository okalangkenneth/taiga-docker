cat > settings/local.py << 'EOF'
from .config import *

# your site-specific overrides go here
# django-cors-headers
INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

# enable django-cors-headers
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_METHODS = [
    "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS",
]
CORS_ALLOW_HEADERS = [
    "Authorization", "Content-Type", "X-Requested-With",
]
EOF
