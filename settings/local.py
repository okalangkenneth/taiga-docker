# Add CORS support
INSTALLED_APPS += ["corsheaders"]

# Add CORS middleware - it must be placed as high as possible
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

# Allow requests from your React app
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# For development, you can also enable this (but don't use in production)
# CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

# Additional headers that might be needed
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "x-session-id",
    "x-lazy-pagination",
    "x-disable-pagination",
    "set-orders",
]
