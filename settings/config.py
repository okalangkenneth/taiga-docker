 # ── Add corsheaders to INSTALLED_APPS ─────────────────────────────────────
 INSTALLED_APPS += [
     "corsheaders",
 ]

 # ── Insert middleware at the very top ─────────────────────────────────────
 MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

+# ── django‑cors‑headers settings ──────────────────────────────────────────
+# require pip install django-cors-headers in your taiga-back image
+CORS_ALLOWED_ORIGINS = [
+    "http://localhost:3000",
+]
+CORS_ALLOW_METHODS = [
+    "GET",
+    "POST",
+    "PUT",
+    "PATCH",
+    "DELETE",
+    "OPTIONS",
+]
+CORS_ALLOW_HEADERS = [
+    "Authorization",
+    "Content-Type",
+]

