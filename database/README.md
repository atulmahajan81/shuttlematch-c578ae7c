# ShuttleMatch Database

This document provides an overview of the database schema for the ShuttleMatch application, including information on the tables, their columns, relationships, and indexes.

## Schema Overview

- **Users**: Represents a user in the system with attributes like email, password hash, and role.
- **Tournaments**: Represents a badminton tournament with attributes like name, location, and date.
- **Matches**: Represents matches in a tournament, including scheduled time and player associations.
- **Scores**: Represents scores for each match.

## Database Setup

1. Ensure PostgreSQL is installed and running on your machine.
2. Create a database named `dbname`.
3. Use the provided `schema.sql` file to create the necessary tables and triggers.
4. Use Alembic to apply migrations:
   ```bash
   alembic upgrade head
   ```
5. Seed the database with initial data using either the Python script `seed_data.py` or SQL `seed_data.sql`.
6. Configure the application to connect to the database using the connection string in `alembic.ini`.

## Indexes and Performance

- Indexes are created on important columns like email, tournament_id, and scheduled_time to optimize query performance.
- Composite and partial indexes are used to improve scalability and speed for common query patterns.

## Triggers

- A trigger is set up on each table to automatically update the `updated_at` timestamp when a record is modified.

## Async Configuration

- Alembic is configured to work with SQLAlchemy asynchronously using `asyncpg`.
- The `env.py` file is set up to handle both offline and online migrations.

## Seeding Data

- Seed data can be added using the `seed_data.py` script which connects to the database asynchronously.
- Alternatively, the `seed_data.sql` script can be used for direct SQL injection of seed data.