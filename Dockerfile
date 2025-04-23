# Dockerfile.custom
FROM taigaio/taiga-back:latest

# Install django-cors-headers so your local.py CORS settings take effect
RUN pip install django-cors-headers

# Copy your CORS override into the container
COPY settings/local.py /taiga-back/settings/local.py

# (Optional) ensure correct ownership
# RUN chown taiga:taiga /taiga-back/settings/local.py
