# Dockerfile.custom
FROM taigaio/taiga-back:latest

USER root
RUN pip install django-cors-headers
USER taiga

# copy your overrides into the container
COPY settings/config.py/taiga-back/settings/config.py
COPY settings/local.py/taiga-back/settings/local.py

