# Use Python 3.8 as the base image
FROM python:3.8-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Install xsdata with all dependencies
RUN pip install "xsdata==22.7"

# Create a non-root user
RUN useradd -m appuser && \
    chown -R appuser /app
USER appuser

# Command to keep container running
CMD ["python3"]