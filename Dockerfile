FROM python:3.9-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 5000

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run tests during build to ensure image quality
RUN python -m pytest test_app.py -v

# Expose the port the app runs on
EXPOSE $PORT

# Use gunicorn for production
CMD gunicorn --bind 0.0.0.0:$PORT app:app

	