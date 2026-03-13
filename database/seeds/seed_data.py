import asyncio
import asyncpg
from datetime import datetime, timedelta
import uuid

async def seed_data():
    conn = await asyncpg.connect(user='user', password='password',
                                 database='dbname', host='127.0.0.1')

    # Insert users
    await conn.execute('''
        INSERT INTO users (id, email, password_hash, role, created_at, updated_at) VALUES
        ($1, $2, $3, $4, $5, $6),
        ($7, $8, $9, $10, $11, $12),
        ($13, $14, $15, $16, $17, $18)
    ''',
        uuid.uuid4(), 'admin@example.com', 'hashed_password', 'admin', datetime.now() - timedelta(days=10), datetime.now() - timedelta(days=5),
        uuid.uuid4(), 'user1@example.com', 'hashed_password', 'user', datetime.now() - timedelta(days=20), datetime.now() - timedelta(days=15),
        uuid.uuid4(), 'user2@example.com', 'hashed_password', 'user', datetime.now() - timedelta(days=30), datetime.now() - timedelta(days=25))

    # Insert tournaments
    await conn.execute('''
        INSERT INTO tournaments (id, name, location, date, created_at, updated_at) VALUES
        ($1, $2, $3, $4, $5, $6),
        ($7, $8, $9, $10, $11, $12)
    ''',
        uuid.uuid4(), 'Summer Open', 'New York', datetime.now().date() - timedelta(days=5), datetime.now() - timedelta(days=10), datetime.now() - timedelta(days=5),
        uuid.uuid4(), 'Winter Cup', 'Los Angeles', datetime.now().date() - timedelta(days=15), datetime.now() - timedelta(days=20), datetime.now() - timedelta(days=15))

    # Closing connection
    await conn.close()

if __name__ == '__main__':
    asyncio.run(seed_data())