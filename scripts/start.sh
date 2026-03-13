#!/bin/bash

# Check prerequisites
if ! command -v docker &> /dev/null
then
    echo "Docker could not be found. Please install Docker."
    exit
fi

if ! command -v docker-compose &> /dev/null
then
    echo "Docker Compose could not be found. Please install Docker Compose."
    exit
fi

# Start services
set -e
docker-compose up