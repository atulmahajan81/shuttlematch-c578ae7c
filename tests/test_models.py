# test_models.py
import pytest
from sqlalchemy.exc import IntegrityError
from backend.models import User, Tournament, Match, Score
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_user_model_constraints(db_session: AsyncSession):
    """Test User model unique constraint on email field"""
    user1 = User(email="duplicate@test.com", password_hash="hashedpassword", role="user")
    user2 = User(email="duplicate@test.com", password_hash="hashedpassword", role="user")
    db_session.add(user1)
    await db_session.commit()
    db_session.add(user2)
    with pytest.raises(IntegrityError):
        await db_session.commit()

@pytest.mark.asyncio
async def test_tournament_model_relationship(db_session: AsyncSession):
    """Test Tournament model has many Matches relationship"""
    tournament = Tournament(name="Test Tournament", location="Test Location", date="2023-10-01")
    match = Match(tournament_id=tournament.id, player1_id="1", player2_id="2", scheduled_time="2023-10-01T10:00:00")
    tournament.matches.append(match)
    db_session.add(tournament)
    await db_session.commit()
    assert len(tournament.matches) == 1

@pytest.mark.asyncio
async def test_match_model_relationship(db_session: AsyncSession):
    """Test Match model belongs to Tournament relationship"""
    tournament = Tournament(name="Test Tournament", location="Test Location", date="2023-10-01")
    match = Match(tournament_id=tournament.id, player1_id="1", player2_id="2", scheduled_time="2023-10-01T10:00:00")
    db_session.add(tournament)
    db_session.add(match)
    await db_session.commit()
    assert match.tournament_id == tournament.id