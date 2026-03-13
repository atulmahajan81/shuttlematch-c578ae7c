from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import EmailStr, constr

from backend.auth import (create_access_token, create_refresh_token,
                         get_password_hash, verify_password)
from backend.dependencies import get_db
from backend.exceptions import NotFoundException
from backend.models import User
from backend.schemas import TokenOut, UserCreate, UserOut
from backend.tasks import send_email_task

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
async def register(user_create: UserCreate, db: AsyncSession = Depends(get_db)) -> UserOut:
    if len(user_create.password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password too short")
    hashed_password = get_password_hash(user_create.password)
    db_user = User(email=user_create.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    send_email_task.delay(db_user.email)
    return UserOut.from_orm(db_user)

@router.post("/login", response_model=TokenOut)
async def login(form_data: UserCreate, d