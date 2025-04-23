# Use a base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run tests (optional for build validation)
# RUN pytest

# Default command
CMD ["python", "calculator.py"]

