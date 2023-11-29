# Use the official Python image as a base
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /workspace

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose port for server (if applicable)
EXPOSE 8000
