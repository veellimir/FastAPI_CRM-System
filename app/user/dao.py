from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.repository.base import BaseDAO
from core.settings.database import AsyncSessionLocal
from .models import User


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def update_user_avatar(cls, user_id: int, filename: str):
        async with AsyncSessionLocal() as session:
            # Получаем пользователя по идентификатору
            # stmt = select(User).options(selectinload(User)).where(User.id == user_id)
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()

            if user is None:
                raise ValueError("Пользователь не найден.")

            # Устанавливаем новое значение пути к изображению
            user.image = filename

            # session.add(user)
            # await session.flush()

            await session.commit()
