from pydantic import BaseModel, UUID4, Field, ConfigDict
from datetime import datetime
from typing import Literal

class TokenOut(BaseModel):
    access_token: str
    token_type: Literal['bearer']


class UserCreate(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: UUID4
    email: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TournamentCreate(BaseModel):
    name: str
    location: str
    date: datetime


class TournamentUpdate(BaseModel):
    name: str = None
    location: str = None
    date: datetime = None


class TournamentOut(BaseModel):
    id: UUID4
    name: str
    location: str
    date: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class MatchCreate(BaseModel):
    tournament_id: UUID4
    player1_id: UUID4
    player2_id: UUID4
    scheduled_time: datetime


class MatchUpdate(BaseModel):
    scheduled_time: datetime = None


class MatchOut(BaseModel):
    id: UUID4
    tournament_id: UUID4
    player1_id: UUID4
    player2_id: UUID4
    scheduled_time: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ScoreCreate(BaseModel):
    match_id: UUID4
    player1_score: int
    player2_score: int


class ScoreUpdate(BaseModel):
    player1_score: int = None
    player2_score: int = None


class ScoreOut(BaseModel):
    id: UUID4
    match_id: UUID4
    player1_score: int
    player2_score: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)