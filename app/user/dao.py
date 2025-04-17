from sqlalchemy import select

from core.repository import BaseDAO
from core.settings.database import AsyncSessionLocal

from .models import User

from app.exceptions import EXCEPTION_USER_HTTP_404


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def update_user_avatar(cls, user_id: int, filename: str):
        """Сохраняет изображение пользователя"""
        async with AsyncSessionLocal() as session:
            query  = select(User).where(User.id == user_id)
            result = await session.execute(query)
            user = result.scalars().first()

            if user is None:
                raise EXCEPTION_USER_HTTP_404

            user.image = filename
            await session.commit()
