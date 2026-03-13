# test_matches.py

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_match(client: AsyncClient):
    """Test match creation for a tournament."""
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
    create_tournament_response = await client.post(
        "/api/v1/tournaments",
        headers=headers,
        json={"name": "Test Tournament", "location": "Test Location", "date": "2023-01-01"}
    )
    tournament_id = create_tournament_response.json()["id"]
    # Create match
    response = await client.post(
        "/api/v1/matches",
        headers=headers,
        json={"tournament_id": tournament_id, "player1_id": "uuid1", "player2_id": "uuid2", "scheduled_time": "2023-01-01T10:00:00"}
    )
    assert response.status_code == 200
    assert response.json()["tournament_id"] == tournament_id


@pytest.mark.asyncio
async def test_get_match_details(client: AsyncClient):
    """Test retrieving match details."""
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
    create_tournament_response = await client.post(
        "/api/v1/tournaments",
        headers=headers,
        json={"name": "Test Tournament", "location": "Test Location", "date": "2023-01-01"}
    )
    tournament_id = create_tournament_response.json()["id"]
    # Create match
    create_match_response = await client.post(
        "/api/v1/matches",
        headers=headers,
        json={"tournament_id": tournament_id, "player1_id": "uuid1", "player2_id": "uuid2", "scheduled_time": "2023-01-01T10:00:00"}
    )
    match_id = create_match_response.json()["id"]
    # Get match details
    response = await client.get(
        f"/api/v1/matches/{match_id}",
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["id"] == match_id


@pytest.mark.asyncio
async def test_update_match_score(client: AsyncClient):
    """Test updating match score."""
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
    create_tournament_response = await client.post(
        "/api/v1/tournaments",
        headers=headers,
        json={"name": "Test Tournament", "location": "Test Location", "date": "2023-01-01"}
    )
    tournament_id = create_tournament_response.json()["id"]
    # Create match
    create_match_response = await client.post(
        "/api/v1/matches",
        headers=headers,
        json={"tournament_id": tournament_id, "player1_id": "uuid1", "player2_id": "uuid2", "scheduled_time": "2023-01-01T10:00:00"}
    )
    match_id = create_match_response.json()["id"]
    # Update match score
    response = await client.put(
        f"/api/v1/matches/{match_id}/score",
        headers=headers,
        json={"player1_score": 21, "player2_score": 19}
    )
    assert response.status_code == 200
    assert response.json()["player1_score"] == 21
    assert response.json()["player2_score"] == 19