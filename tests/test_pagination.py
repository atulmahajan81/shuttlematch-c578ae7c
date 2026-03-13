# test_pagination.py

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_pagination_on_list_tournaments(client: AsyncClient):
    """Test pagination on list tournaments endpoint."""
    # Register and login the user
    await client.post(
        "/api/v1/auth/register",
        json={"email": "pagination@example.com", "password": "strongpassword", "role": "user"}
    )
    login_response = await client.post(
        "/api/v1/auth/login",
        json={"email": "pagination@example.com", "password": "strongpassword"}
    )
    access_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}

    # Create multiple tournaments
    for i in range(5):
        await client.post(
            "/api/v1/tournaments",
            headers=headers,
            json={"name": f"Tournament {i}", "location": "City", "date": "2023-01-01"}
        )

    # Test pagination
    response = await client.get(
        "/api/v1/tournaments",
        headers=headers,
        params={"page": 1, "limit": 2}
    )
    assert response.status_code == 200
    assert len(response.json()) == 2