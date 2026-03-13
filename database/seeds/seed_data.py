import asyncio
import asyncpg
from datetime import datetime, timedelta

async def seed_database():
    conn = await asyncpg.connect(user='user', password='password', database='shuttlematch', host='127.0.0.1')

    await conn.execute("""
        INSERT INTO users (email, password_hash, role) VALUES
        ('admin@example.com', 'hashed_password1', 'admin'),
        ('user1@example.com', 'hashed_password2', 'user'),
        ('user2@example.com', 'hashed_password3', 'user');
    """)

    await conn.execute("""
        INSERT INTO tournaments (name, location, date) VALUES
        ('Spring Open', 'Sports Complex', '2023-11-01'),
        ('Summer Classic', 'City Arena', '2023-11-15');
    """)

    # Insert matches
    await conn.execute("""
        INSERT INTO matches (tournament_id, player1_id, player2_id, scheduled_time) VALUES
        ((SELECT id FROM tournaments WHERE name = 'Spring Open'), (SELECT id FROM users WHERE email = 'user1@example.com'), (SELECT id FROM users WHERE email = 'user2@example.com'), '2023-11-01 10:00:00'),
        ((SELECT id FROM tournaments WHERE name = 'Summer Classic'), (SELECT id FROM users WHERE email = 'user1@example.com'), (SELECT id FROM users WHERE email = 'user2@example.com'), '2023-11-15 12:00:00');
    """)

    # Insert scores
    await conn.execute("""
        INSERT INTO scores (match_id, player1_score, player2_score) VALUES
        ((SELECT id FROM matches WHERE scheduled_time = '2023-11-01 10:00:00'), 21, 15),
        ((SELECT id FROM matches WHERE scheduled_time = '2023-11-15 12:00:00'), 18, 21);
    """)

    await conn.close()

asyncio.run(seed_database())