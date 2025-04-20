# Ethereum Dockerfile
FROM python:3.10-slim

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install web3 and solcx
RUN pip install --no-cache-dir web3 py-solc-x

# Set environment variable for Python buffer
ENV PYTHONUNBUFFERED=1

# Default command (you can override this in docker-compose)
CMD ["python", "deploy_contract.py"]
