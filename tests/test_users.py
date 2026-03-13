# test_users.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_user_profile(async_client: AsyncClient, auth_headers):
    """Test retrieving user profile with valid token"""
    response = await async_client.get("/api/v1/users/profile", headers=auth_headers)
    assert response.status_code == 200
    assert "id" in response.json()
    assert "email" in response.json()

@pytest.mark.asyncio
async def test_update_user_profile(async_client: AsyncClient, auth_headers):
    """Test updating user profile with valid data"""
    response = await async_client.put("/api/v1/users/profile", json={"email": "newemail@test.com", "password": "newpassword123"}, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["email"] == "newemail@test.com"

@pytest.mark.asyncio
async def test_update_user_profile_unauthorized(async_client: AsyncClient):
    """Test updating user profile without authentication"""
    response = await async_client.put("/api/v1/users/profile", json={"email": "newemail@test.com", "password": "newpassword123"})
    assert response.status_code == 401