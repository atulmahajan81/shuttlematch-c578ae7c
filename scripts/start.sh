#!/bin/bash

set -e

# Check prerequisites
if ! command -v docker &> /dev/null
then
    echo "Docker could not be found"
    exit
fi

if ! command -v docker-compose &> /dev/null
then
    echo "docker-compose could not be found"
    exit
fi

# Start services
docker-compose up --build