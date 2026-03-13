from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import select
from fastapi import Depends, HTTPException, status

from .config import settings

Base = declarative_base()

engine = create_async_engine(settings.DATABASE_URL, pool_size=5, max_overflow=10, pool_timeout=30)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

def get_db():
    db = async_session()
    try:
        yield db
    finally:
        db.close()