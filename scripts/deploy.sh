#!/bin/bash

set -e

# Pull latest images
ssh $PRODUCTION_USER@$PRODUCTION_SERVER "cd /path/to/deployment && git pull && docker-compose pull && docker-compose up -d"