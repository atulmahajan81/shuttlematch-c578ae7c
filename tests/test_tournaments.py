# test_tournaments.py

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_tournament(client: AsyncClient):
    """Test tournament creation with valid data."""
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
    # Create tournament
    response = await client.post(
        "/api/v1/tournaments",
        headers=headers,
        json={"name": "Test Tournament", "location": "Test Location", "date": "2023-01-01"}
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Test Tournament"


@pytest.mark.asyncio
async def test_list_tournaments(client: AsyncClient):
    """Test listing all tournaments."""
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
    # List tournaments
    response = await client.get(
        "/api/v1/tournaments",
        headers=headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_tournament_details(client: AsyncClient):
    """Test retrieving tournament details."""
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
    # Create tournament
    create_response = await client.post(
        "/api/v1/tournaments",
        headers=headers,
        json={"name": "Test Tournament", "location": "Test Location", "date": "2023-01-01"}
    )
    tournament_id = create_response.json()["id"]
    # Get tournament details
    response = await client.get(
        f"/api/v1/tournaments/{tournament_id}",
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["id"] == tournament_id