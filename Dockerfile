# Use the official Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY siri.py .

# Run the Python script when the container starts
CMD ["python", "siri.py"]
