# test_integration.py

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_full_user_flow(client: AsyncClient):
    """Test full user flow from registration to tournament creation."""
    # Register the user
    register_response = await client.post(
        "/api/v1/auth/register",
        json={"email": "flow@example.com", "password": "strongpassword", "role": "user"}
    )
    assert register_response.status_code == 200
    user_id = register_response.json()["id"]

    # Login the user
    login_response = await client.post(
        "/api/v1/auth/login",
        json={"email": "flow@example.com", "password": "strongpassword"}
    )
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}

    # Create a tournament
    create_tournament_response = await client.post(
        "/api/v1/tournaments",
        headers=headers,
        json={"name": "Full Flow Tournament", "location": "Test City", "date": "2023-01-01"}
    )
    assert create_tournament_response.status_code == 200
    tournament_id = create_tournament_response.json()["id"]

    # Retrieve tournament details
    tournament_details_response = await client.get(
        f"/api/v1/tournaments/{tournament_id}",
        headers=headers
    )
    assert tournament_details_response.status_code == 200
    assert tournament_details_response.json()["id"] == tournament_id

    # Logout
    logout_response = await client.post(
        "/api/v1/auth/logout",
        headers=headers
    )
    assert logout_response.status_code == 200
    assert logout_response.json()["message"] == "Successfully logged out"