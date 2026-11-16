
FROM nginx:1.27-alpine

# Copy the complete frontend website into Nginx
COPY . /usr/share/nginx/html/

# Copy the Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose the website port
EXPOSE 80
