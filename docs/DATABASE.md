# Database Documentation

## Schema Overview

The ShuttleMatch database schema is designed to support tournament management with entities for users, tournaments, matches, and scores.

### Entity Relationships

- **User**: Represents a participant in the system, either as an organizer, player, or umpire.
- **Tournament**: Contains information about tournaments, including location and date.
- **Match**: Represents individual matches within a tournament.
- **Score**: Tracks the scores associated with matches.

### Diagram

```mermaid
erDiagram
  User {
    UUID id
    string email
    string role
  }
  Tournament {
    UUID id
    string name
    string location
    string date
  }
  Match {
    UUID id
    UUID tournament_id
    UUID player1_id
    UUID player2_id
    string scheduled_time
  }
  Score {
    UUID match_id
    int player1_score
    int player2_score
  }

  User ||--o{ Match : player1
  User ||--o{ Match : player2
  Tournament ||--o{ Match : contains
  Match ||--o{ Score : has
```

## Migration Guide

- Use `Alembic` for managing database migrations.
- To create a new migration:
  ```bash
  alembic revision --autogenerate -m "Description of changes"
  ```
- To apply migrations:
  ```bash
  alembic upgrade head
  ```