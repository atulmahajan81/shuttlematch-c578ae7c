# test_auth.py

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    """Test user registration endpoint with valid data."""
    response = await client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "strongpassword", "role": "user"}
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_register_user_invalid_data(client: AsyncClient):
    """Test user registration endpoint with invalid email."""
    response = await client.post(
        "/api/v1/auth/register",
        json={"email": "invalid-email", "password": "password", "role": "user"}
    )
    assert response.status_code == 422
    assert "detail" in response.json()


@pytest.mark.asyncio
async def test_login_user(client: AsyncClient):
    """Test user login endpoint with valid credentials."""
    # First, register the user
    await client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "strongpassword", "role": "user"}
    )
    # Then, login
    response = await client.post(
        "/api/v1/auth/login",
        json={"email": "test@example.com", "password": "strongpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()


@pytest.mark.asyncio
async def test_login_user_invalid_credentials(client: AsyncClient):
    """Test user login endpoint with invalid credentials."""
    response = await client.post(
        "/api/v1/auth/login",
        json={"email": "nonexistent@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    assert "detail" in response.json()


@pytest.mark.asyncio
async def test_refresh_token(client: AsyncClient):
    """Test JWT token refresh with valid refresh token."""
    # Register and login the user
    await client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "strongpassword", "role": "user"}
    )
    login_response = await client.post(
        "/api/v1/auth/login",
        json={"email": "test@example.com", "password": "strongpassword"}
    )
    refresh_token = login_response.json()["refresh_token"]
    # Refresh token
    response = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": refresh_token}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.asyncio
async def test_logout_user(client: AsyncClient):
    """Test user logout endpoint."""
    # Register and login the user
    await client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "strongpassword", "role": "user"}
    )
    login_response = await client.post(
        "/api/v1/auth/login",
        json={"email": "test@example.com", "password": "strongpassword"}
    )
    access_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    # Logout
    response = await client.post(
        "/api/v1/auth/logout",
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Successfully logged out"