# test_pagination.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_tournament_pagination(async_client: AsyncClient, auth_headers):
    """Test pagination on tournament list endpoint"""
    # Create multiple tournaments
    for i in range(15):
        await async_client.post("/api/v1/tournaments", json={"name": f"Tournament {i}", "location": "Location", "date": "2023-10-01"}, headers=auth_headers)
    response = await async_client.get("/api/v1/tournaments?page=1&limit=10", headers=auth_headers)
    assert response.status_code == 200
    tournaments = response.json()
    assert len(tournaments) == 10

@pytest.mark.asyncio
async def test_tournament_sorting(async_client: AsyncClient, auth_headers):
    """Test sorting on tournament list endpoint"""
    response = await async_client.get("/api/v1/tournaments?page=1&limit=10", headers=auth_headers)
    assert response.status_code == 200
    tournaments = response.json()
    assert tournaments == sorted(tournaments, key=lambda x: x["date"])