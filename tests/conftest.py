# conftest.py

import asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from backend.main import app
from backend.database import Base, get_async_session

# Database setup
DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def async_session():
    """Create a new database session for a test."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as session:
        yield session

@pytest.fixture(scope="function")
async def client(async_session: AsyncSession):
    """Create a new HTTP client for a test."""
    async def get_test_db():
        yield async_session

    app.dependency_overrides[get_async_session] = get_test_db
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client