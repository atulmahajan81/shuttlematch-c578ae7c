from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from ..models import Tournament
from ..schemas import TournamentCreate, TournamentRead
from ..services.tournament_service import create_tournament, get_tournament, list_tournaments
from ..database import get_async_session
from ..dependencies import get_current_user

router = APIRouter(prefix="/api/v1/tournaments", tags=["tournaments"])


@router.post("/", response_model=TournamentRead, status_code=status.HTTP_201_CREATED)
async def create_tournament_endpoint(
    tournament: TournamentCreate,
    session: AsyncSession = Depends(get_async_session),
    current_user: dict = Depends(get_current_user),
):
    """
    Create a new tournament
    """
    return await create_tournament(session, tournament)


@router.get("/", response_model=list[TournamentRead])
async def list_tournaments_endpoint(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_async_session),
    current_user: dict = Depends(get_current_user),
):
    """
    List all tournaments
    """
    return await list_tournaments(session, skip=skip, limit=limit)


@router.get("/{tournament_id}", response_model=TournamentRead)
async def get_tournament_endpoint(
    tournament_id: UUID,
    session: AsyncSession = Depends(get_async_session),
    current_user: dict = Depends(get_current_user),
):
    """
    Get tournament details
    """
    tournament = await get_tournament(session, tournament_id)
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tournament not found")
    return tournament