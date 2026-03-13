# ShuttleMatch Database

This document outlines the database schema for ShuttleMatch, a sports management platform for badminton tournaments.

## Schema Diagram Description

- **Users**: Contains user information. Each user has a unique email, password hash, and role (either 'admin' or 'user').
- **Tournaments**: Details of badminton tournaments, including name, location, and date. Each tournament can have multiple matches.
- **Matches**: Represents a match between two players in a tournament. It stores references to the tournament and the players participating.
- **Scores**: Stores the scores for each match.

## Setup Instructions

1. **Database Initialization**:
   - Ensure PostgreSQL is installed and running.
   - Run the schema.sql to create the database schema.

   ```bash
   psql -U your_username -d shuttlematch -f database/schema.sql
   ```

2. **Apply Migrations**:
   - Configure your database URL in `alembic.ini`.
   - Run Alembic migrations to ensure the database is up to date.

   ```bash
   alembic upgrade head
   ```

3. **Seed Data**:
   - Insert initial data using the provided seed scripts.

   ```bash
   python database/seeds/seed_data.py
   ```
   or
   ```bash
   psql -U your_username -d shuttlematch -f database/seeds/seed_data.sql
   ```

## Scalability Considerations

- **Caching Strategy**: Implement Redis caching for frequently accessed data, with a 5-minute TTL.
- **Database Indexing**: Indexes are created on email, tournament_id, and scheduled_time for performance optimization.
- **Asynchronous Tasks**: Use Celery for handling background jobs efficiently.