# Dockerfile.custom
FROM taigaio/taiga-back:latest

USER root

# install django-cors-headers
RUN pip install django-cors-headers

USER taiga
