# Use Python 3.11.4 slim image
FROM python:3.11.4-slim

# Set working directory
WORKDIR /flask_docker

# Copy requirements first (best for caching layers)
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to the working directory
COPY . .

# Expose port for Flask
EXPOSE 5000

# Run Flask app
CMD ["flask", "--app", "Car_pred.py", "run", "--host=0.0.0.0"]
