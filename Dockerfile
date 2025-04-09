# Dockerfile

FROM python:3.8-slim

WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies with an increased timeout (e.g., 120 seconds)
RUN pip install --default-timeout=120 --no-cache-dir -r requirements.txt

# Optionally expose a port (if needed)
# EXPOSE 5000

CMD ["python", "main.py"]
