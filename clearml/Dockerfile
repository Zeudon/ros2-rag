FROM allegroai/clearml:latest

# Set environment variables for ClearML server configuration
ENV CLEARML_APISERVER_HOST=http://localhost:8008
ENV CLEARML_WEB_HOST=http://localhost:8080
ENV CLEARML_FILES_HOST=http://localhost:8081

# Expose required ports
EXPOSE 8008 8080 8081

# Start all ClearML services (apiserver, webserver, fileserver)
CMD ["/bin/bash", "-c", "/entrypoint.sh apiserver & /entrypoint.sh webserver & /entrypoint.sh fileserver && wait"]
