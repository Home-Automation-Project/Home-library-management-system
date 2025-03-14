# Use an official Python base image
FROM python:3.11-slim

# Set environment variables for CouchDB (can be overridden at runtime)
ARG COUCHDB_USER=admin
ARG COUCHDB_PASSWORD=password
ENV COUCHDB_USER=$COUCHDB_USER
ENV COUCHDB_PASSWORD=$COUCHDB_PASSWORD

# Install dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install FastAPI and dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install CouchDB
RUN apt-get update && apt-get install -y couchdb && rm -rf /var/lib/apt/lists/*

# Configure CouchDB
RUN mkdir -p /etc/couchdb/local.d \
    && echo "[chttpd]\nbind_address = 0.0.0.0\nport = 5984" > /etc/couchdb/local.d/custom.ini \
    && echo "[admins]\n$COUCHDB_USER = $COUCHDB_PASSWORD" > /opt/couchdb/etc/local.ini

# Expose CouchDB and FastAPI ports
EXPOSE 8000 5984

# Copy FastAPI app
COPY . /app

# Start CouchDB and FastAPI together
CMD service couchdb start && uvicorn main:app --host 0.0.0.0 --port 8000