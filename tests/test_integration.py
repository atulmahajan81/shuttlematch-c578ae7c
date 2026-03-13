# test_integration.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_user_flow(async_client: AsyncClient):
    """Test complete user registration and profile update flow"""
    # Register
    register_response = await async_client.post("/api/v1/auth/register", json={"email": "flow@test.com", "password": "flowpass", "role": "user"})
    assert register_response.status_code == 200
    user_id = register_response.json()["id"]
    # Login
    login_response = await async_client.post("/api/v1/auth/login", json={"email": "flow@test.com", "password": "flowpass"})
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    # Profile update
    update_response = await async_client.put("/api/v1/users/profile", json={"email": "flowupdated@test.com", "password": "newflowpass"}, headers=headers)
    assert update_response.status_code == 200
    assert update_response.json()["email"] == "flowupdated@test.com"