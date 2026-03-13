# test_matches.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_match(async_client: AsyncClient, auth_headers):
    """Test creating a new match within a tournament"""
    # Create a tournament first
    tournament_response = await async_client.post("/api/v1/tournaments", json={"name": "Summer Open", "location": "Central Park", "date": "2023-08-15"}, headers=auth_headers)
    tournament_id = tournament_response.json()["id"]
    # Create players
    player1_response = await async_client.post("/api/v1/auth/register", json={"email": "player1@test.com", "password": "password123", "role": "player"})
    player1_id = player1_response.json()["id"]
    player2_response = await async_client.post("/api/v1/auth/register", json={"email": "player2@test.com", "password": "password123", "role": "player"})
    player2_id = player2_response.json()["id"]
    # Create match
    response = await async_client.post("/api/v1/matches", json={"tournament_id": tournament_id, "player1_id": player1_id, "player2_id": player2_id, "scheduled_time": "2023-08-15T10:00:00"}, headers=auth_headers)
    assert response.status_code == 200
    assert "id" in response.json()

@pytest.mark.asyncio
async def test_get_match_details(async_client: AsyncClient, auth_headers):
    """Test retrieving match details with valid match ID"""
    # Create a match first
    tournament_response = await async_client.post("/api/v1/tournaments", json={"name": "Summer Open", "location": "Central Park", "date": "2023-08-15"}, headers=auth_headers)
    tournament_id = tournament_response.json()["id"]
    player1_response = await async_client.post("/api/v1/auth/register", json={"email": "player1@test.com", "password": "password123", "role": "player"})
    player1_id = player1_response.json()["id"]
    player2_response = await async_client.post("/api/v1/auth/register", json={"email": "player2@test.com", "password": "password123", "role": "player"})
    player2_id = player2_response.json()["id"]
    match_response = await async_client.post("/api/v1/matches", json={"tournament_id": tournament_id, "player1_id": player1_id, "player2_id": player2_id, "scheduled_time": "2023-08-15T10:00:00"}, headers=auth_headers)
    match_id = match_response.json()["id"]
    # Get match details
    response = await async_client.get(f"/api/v1/matches/{match_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == match_id

@pytest.mark.asyncio
async def test_update_match_score(async_client: AsyncClient, auth_headers):
    """Test updating match score with valid data"""
    # Create a match first
    tournament_response = await async_client.post("/api/v1/tournaments", json={"name": "Summer Open", "location": "Central Park", "date": "2023-08-15"}, headers=auth_headers)
    tournament_id = tournament_response.json()["id"]
    player1_response = await async_client.post("/api/v1/auth/register", json={"email": "player1@test.com", "password": "password123", "role": "player"})
    player1_id = player1_response.json()["id"]
    player2_response = await async_client.post("/api/v1/auth/register", json={"email": "player2@test.com", "password": "password123", "role": "player"})
    player2_id = player2_response.json()["id"]
    match_response = await async_client.post("/api/v1/matches", json={"tournament_id": tournament_id, "player1_id": player1_id, "player2_id": player2_id, "scheduled_time": "2023-08-15T10:00:00"}, headers=auth_headers)
    match_id = match_response.json()["id"]
    # Update match score
    response = await async_client.put(f"/api/v1/matches/{match_id}/score", json={"player1_score": 21, "player2_score": 15}, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["player1_score"] == 21
    assert response.json()["player2_score"] == 15