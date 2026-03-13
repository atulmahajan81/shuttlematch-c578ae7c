# test_auth.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_user(async_client: AsyncClient):
    """Test user registration with valid data"""
    response = await async_client.post("/api/v1/auth/register", json={"email": "user@test.com", "password": "password123", "role": "user"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["email"] == "user@test.com"

@pytest.mark.asyncio
@pytest.mark.parametrize("payload,expected_status", [
    ({"email": "", "password": "password123", "role": "user"}, 422),
    ({"email": "user@test.com", "password": "", "role": "user"}, 422),
    ({"email": "user@test.com", "password": "password123", "role": ""}, 422)
])
async def test_register_user_invalid_data(async_client: AsyncClient, payload, expected_status):
    """Test user registration with invalid data"""
    response = await async_client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == expected_status

@pytest.mark.asyncio
async def test_login_user(async_client: AsyncClient):
    """Test login with valid credentials"""
    await async_client.post("/api/v1/auth/register", json={"email": "login@test.com", "password": "password123", "role": "user"})
    response = await async_client.post("/api/v1/auth/login", json={"email": "login@test.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

@pytest.mark.asyncio
async def test_refresh_token(async_client: AsyncClient, auth_headers):
    """Test refreshing JWT token with valid refresh token"""
    refresh_response = await async_client.post("/api/v1/auth/refresh", json={}, headers=auth_headers)
    assert refresh_response.status_code == 200
    assert "access_token" in refresh_response.json()

@pytest.mark.asyncio
async def test_logout_user(async_client: AsyncClient, auth_headers):
    """Test logout user and invalidate token"""
    logout_response = await async_client.post("/api/v1/auth/logout", headers=auth_headers)
    assert logout_response.status_code == 200
    assert logout_response.json()["message"] == "Successfully logged out"