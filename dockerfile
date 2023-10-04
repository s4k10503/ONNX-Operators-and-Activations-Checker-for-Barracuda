# Base image
FROM python:3.8-slim-buster

# Setting environment variables
ENV DISPLAY=unix$DISPLAY \
    DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python library
RUN pip install --no-cache-dir \
    onnx \
    customtkinter

# Copy the application code
COPY . /app
WORKDIR /app

# Run application
CMD ["python", "main.py"]
