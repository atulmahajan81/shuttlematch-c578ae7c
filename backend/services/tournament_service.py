from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from ..models import Tournament
from ..schemas import TournamentCreate, TournamentRead


async def create_tournament(session: AsyncSession, tournament_data: TournamentCreate) -> TournamentRead:
    new_tournament = Tournament(
        name=tournament_data.name,
        location=tournament_data.location,
        date=tournament_data.date
    )
    session.add(new_tournament)
    await session.commit()
    await session.refresh(new_tournament)
    return TournamentRead.from_orm(new_tournament)


async def get_tournament(session: AsyncSession, tournament_id: UUID) -> TournamentRead:
    query = select(Tournament).where(Tournament.id == tournament_id)
    result = await session.execute(query)
    tournament = result.scalars().first()
    return TournamentRead.from_orm(tournament) if tournament else None


async def list_tournaments(session: AsyncSession, skip: int = 0, limit: int = 10) -> list[TournamentRead]:
    query = select(Tournament).offset(skip).limit(limit)
    result = await session.execute(query)
    tournaments = result.scalars().all()
    return [TournamentRead.from_orm(tournament) for tournament in tournaments]