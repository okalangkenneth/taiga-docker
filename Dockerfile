FROM nginx:1.23

# Remove the default configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy your configuration as a file, not a directory
COPY taiga-nginx.conf /etc/nginx/conf.d/default.conf

# Make sure it's a file
RUN test -f /etc/nginx/conf.d/default.conf || exit 1
