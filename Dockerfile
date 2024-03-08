# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run the app. Modify the IP address (or FQDN) to restrict access to the feed to a specific interface address
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
