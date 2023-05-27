# Use the official Python base image with the desired version and Alpine Linux
FROM python:3.10.2-alpine

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apk update \
    && apk add --no-cache gcc musl-dev

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Set the command to run your Python application
CMD [ "python", "app.py" ]
