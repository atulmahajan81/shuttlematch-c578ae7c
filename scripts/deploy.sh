#!/bin/bash

set -e

# Pull latest changes from the repository
echo "Pulling latest changes..."
ssh -o StrictHostKeyChecking=no $USER@$HOST "cd /path/to/deployment && git pull"

# Deploy the application
ssh -o StrictHostKeyChecking=no $USER@$HOST "cd /path/to/deployment && docker-compose pull && docker-compose up -d --build"

# Run migrations
ssh -o StrictHostKeyChecking=no $USER@$HOST "cd /path/to/deployment && ./scripts/migrate.sh"