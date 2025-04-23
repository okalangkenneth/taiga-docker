# Dockerfile
FROM taigaio/taiga-back:latest

USER root

# Install CORS headers package
RUN pip install django-cors-headers

# Copy in your Django settings overrides
COPY settings/config.py /taiga-back/settings/config.py
COPY settings/local.py  /taiga-back/settings/local.py

USER taiga
