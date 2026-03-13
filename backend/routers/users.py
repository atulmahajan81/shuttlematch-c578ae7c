from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.dependencies import get_current_user, get_db, pagination_params
from backend.exceptions import NotFoundException
from backend.models import User
from backend.schemas import UserOut, UserUpdate

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.get("/", response_model=list[UserOut])
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

@router.put("/{id}", response_model=UserOut)
async def update_user(id: str, user_update: UserUpdate, db: AsyncSession = Depends(get_db)) -> UserOut:
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    if user is None:
        raise NotFoundException(detail="User not found")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserOut.from_orm(user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str, db: AsyncSession = Depends(get_db)) -> None:
    result = await db.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    if user is None:
        raise NotFoundException(detail="User not found")

    await db.delete(user)
    await db.commit()