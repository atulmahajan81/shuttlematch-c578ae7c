#!/bin/bash

set -e

API_HEALTH_CHECK=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health)

if [ "$API_HEALTH_CHECK" -eq 200 ]; then
  echo "API service is healthy."
else
  echo "API service health check failed with status $API_HEALTH_CHECK"
  exit 1
fi

echo "All services are healthy."