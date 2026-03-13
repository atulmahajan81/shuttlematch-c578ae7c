# Deployment Guide

## Docker Deployment

1. **Build Docker Images**:
   ```bash
   docker-compose build
   ```

2. **Run Docker Containers**:
   ```bash
   docker-compose up -d
   ```

## Environment Variables Reference

| Name               | Description                            |
|--------------------|----------------------------------------|
| DATABASE_URL       | Connection string for PostgreSQL       |
| REDIS_URL          | Connection string for Redis            |
| SECRET_KEY         | Secret key for JWT tokens              |
| ACCESS_TOKEN_EXPIRE| Expiration time for access tokens      |

## Scaling Guide

ShuttleMatch can be scaled horizontally by adding more instances of the backend and frontend services. Consider using Docker Swarm or Kubernetes for container orchestration in a production environment.

## Monitoring

- Use `Prometheus` and `Grafana` for monitoring application performance and health.
- Set up alerts for key metrics such as response times and error rates.