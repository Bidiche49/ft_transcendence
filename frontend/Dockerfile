# Use an official nginx image
FROM nginx:alpine

# Set the working directory to nginx's serve directory
WORKDIR /usr/share/nginx/html

# Remove the default nginx static files
RUN rm -rf ./*

# Copy static content from your frontend directory
COPY . /usr/share/nginx/html

# Expose port 80 to the host
EXPOSE 80

# Start nginx and keep it running in the foreground
CMD ["nginx", "-g", "daemon off;"]
