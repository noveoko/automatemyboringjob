 I'll help you create a container with Python 3.8 and xsdata 22.7. I'll create a Dockerfile for this setup.



<antArtifact identifier="python-xsdata-dockerfile" type="application/vnd.ant.code" language="dockerfile" title="Dockerfile for Python 3.8 with xsdata">
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
</antArtifact>

To build and run this container, follow these steps:

1. Create a new directory and save the Dockerfile in it:
```bash
mkdir python-xsdata
cd python-xsdata
# Save the Dockerfile content shown above
```

2. Build the container:
```bash
podman build -t python-xsdata .
```

3. Run the container interactively:
```bash
podman run -it python-xsdata
```

To verify the installation, you can run these commands inside the container:
```python
import sys
import xsdata

print(f"Python version: {sys.version}")
print(f"xsdata version: {xsdata.__version__}")
```

If you want to mount a local directory to work with files, you can use:
```bash
podman run -it -v ./your_local_dir:/app/work python-xsdata
```

Would you like me to show you how to:
1. Add additional Python packages to the container?
2. Create a more production-ready configuration?
3. Set up volume mounts for development?