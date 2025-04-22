# CORS Settings for Taiga Backend
INSTALLED_APPS += ["corsheaders"]

MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

# Allow your React development server
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# Allow credentials if needed (cookies, authorization headers)
CORS_ALLOW_CREDENTIALS = True

# Add any additional headers your React app sends
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
