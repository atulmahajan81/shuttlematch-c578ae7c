from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, Integer, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False, index=True)
    location = Column(String, nullable=False)
    date = Column(TIMESTAMP, nullable=False, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    matches = relationship('Match', back_populates='tournament')


class Match(Base):
    __tablename__ = 'matches'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey('tournaments.id'), nullable=False)
    player1_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    player2_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    tournament = relationship('Tournament', back_populates='matches')