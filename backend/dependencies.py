from typing import Optional

from fastapi import Depends, HTTPException, Query, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.auth import verify_token
from backend.exceptions import NotFoundException, UnauthorizedException
from backend.models import User
from backend.schemas import UserOut
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_db() -> AsyncSession:
    from backend.database import async_session
    async with async_session() as session:
        yield session

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> UserOut:
    credentials_exception = UnauthorizedException(detail="Could not validate credentials")
    payload = verify_token(token, credentials_exception)
    user_id: str = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if user is None:
        raise NotFoundException(detail="User not found")

    return UserOut.from_orm(user)

async def get_current_admin(current_user: UserOut = Depends(get_current_user)) -> UserOut:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges",
        )
    return current_user