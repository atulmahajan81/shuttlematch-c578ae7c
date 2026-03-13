#!/bin/bash

set -e

# Run database migrations
echo "Running database migrations..."
docker-compose run --rm api alembic upgrade head