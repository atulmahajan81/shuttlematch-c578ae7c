from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import User
from ..schemas import UserCreate, UserRead
from ..exceptions import UserAlreadyExistsException
from sqlalchemy.future import select
from backend.cache import redis_cache

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


@redis_cache(ttl=300)
async def create_user(session: AsyncSession, user_data: UserCreate) -> UserRead:
    query = select(User).filter(User.email == user_data.email)
    result = await session.execute(query)
    existing_user = result.scalars().first()
    if existing_user:
        raise UserAlreadyExistsException("User with this email already exists")

    hashed_password = get_password_hash(user_data.password)
    new_user = User(email=user_data.email, hashed_password=hashed_password, role=user_data.role)
    session.add(new_user)
    await session.commit()