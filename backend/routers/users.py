from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.dependencies import get_current_user, get_db, pagination_params
from backend.exceptions import NotFoundException
from backend.models import User
from backend.schemas import UserOut, UserUpdate

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.get("/", response_model=list[UserOut], response_model_exclude_unset=True)
async def read_users(
    db: AsyncSession = Depends(get_db),
    pagination: dict = Depends(pagination_params),
) -> list[UserOut]:
    result = await db.execute(select(User).offset(pagination["skip"]).limit(pagination["limit"]))
    users = result.scalars().all()
    return [UserOut.from_orm(user) for user in users]

@router.get("/{id}", response_model=UserOut)
async def read_user(id: str, db: AsyncSession = Depends(get_db)) -> UserOut:
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    if user is None:
        raise NotFoundException(detail="User not found")
    return UserOut.from_orm(user)