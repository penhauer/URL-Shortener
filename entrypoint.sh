#!/bin/bash

cd /app/src

echo "Starting application with ${WORKERS} workers..."

gunicorn --workers="${WORKERS}" --bind=0.0.0.0:80 main:app
 