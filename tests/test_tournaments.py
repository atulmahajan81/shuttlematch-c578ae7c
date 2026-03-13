# test_tournaments.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_tournament(async_client: AsyncClient, auth_headers):
    """Test creating a new tournament with valid data"""
    response = await async_client.post("/api/v1/tournaments", json={"name": "Open Championship", "location": "City Arena", "date": "2023-10-01"}, headers=auth_headers)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Open Championship"

@pytest.mark.asyncio
async def test_list_tournaments(async_client: AsyncClient, auth_headers):
    """Test listing all tournaments with pagination"""
    response = await async_client.get("/api/v1/tournaments?page=1&limit=10", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_tournament_details(async_client: AsyncClient, auth_headers):
    """Test retrieving tournament details with valid ID"""
    create_response = await async_client.post("/api/v1/tournaments", json={"name": "Open Championship", "location": "City Arena", "date": "2023-10-01"}, headers=auth_headers)
    tournament_id = create_response.json()["id"]
    response = await async_client.get(f"/api/v1/tournaments/{tournament_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == tournament_id