# test_models.py

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import User, Tournament, Match


@pytest.mark.asyncio
async def test_user_model(async_session: AsyncSession):
    """Test the User model for constraints and relationships."""
    user = User(email="unique@example.com", password_hash="hashed_password", role="user")
    async_session.add(user)
    await async_session.commit()

    # Test uniqueness constraint
    with pytest.raises(IntegrityError):
        duplicate_user = User(email="unique@example.com", password_hash="hashed_password", role="user")
        async_session.add(duplicate_user)
        await async_session.commit()


@pytest.mark.asyncio
async def test_tournament_model(async_session: AsyncSession):
    """Test the Tournament model for constraints and relationships."""
    tournament = Tournament(name="Open Tournament", location="City", date="2023-01-01")
    async_session.add(tournament)
    await async_session.commit()


@pytest.mark.asyncio
async def test_match_model(async_session: AsyncSession):
    """Test the Match model for constraints and relationships."""
    tournament = Tournament(name="Open Tournament", location="City", date="2023-01-01")
    async_session.add(tournament)
    await async_session.commit()

    match = Match(
        tournament_id=tournament.id, player1_id="uuid-player1", player2_id="uuid-player2", scheduled_time="2023-01-01T10:00:00"
    )
    async_session.add(match)
    await async_session.commit()