# test_users.py

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_user_profile(client: AsyncClient):
    """Test user profile retrieval with valid token."""
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
    # Get user profile
    response = await client.get(
        "/api/v1/users/profile",
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_update_user_profile(client: AsyncClient):
    """Test user profile update with valid token."""
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
    # Update user profile
    response = await client.put(
        "/api/v1/users/profile",
        headers=headers,
        json={"email": "newemail@example.com", "password": "newpassword"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "newemail@example.com"