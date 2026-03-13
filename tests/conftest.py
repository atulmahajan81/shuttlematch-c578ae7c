# conftest.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from backend.main import app
from backend.database import Base
from unittest.mock import patch

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="function")
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with SessionLocal() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def auth_headers(async_client):
    response = await async_client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "password", "role": "user"})
    assert response.status_code == 200
    login_response = await async_client.post("/api/v1/auth/login", json={"email": "test@example.com", "password": "password"})
    assert login_response.status_code == 200
    tokens = login_response.json()
    return {"Authorization": f"Bearer {tokens['access_token']}"}

# Mock external services if needed
def mock_send_email():
    return True

@pytest.fixture(autouse=True)
async def mock_services():
    with patch("backend.services.user_service.send_email", mock_send_email):
        yield