# Dockerfile

FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy your code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# (Optional) Expose a port if your app runs a server
# EXPOSE 5000

# Default command
CMD ["python", "main.py"]
