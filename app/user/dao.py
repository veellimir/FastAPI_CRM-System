from sqlalchemy import select, or_

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

    @classmethod
    async def search(cls, query_str: str):
        async with AsyncSessionLocal() as session:
            query = select(cls.model).where(or_(
                cls.model.email.ilike(f"%{query_str}%"),
                cls.model.first_name.ilike(f"%{query_str}%"),
                cls.model.last_name.ilike(f"%{query_str}%")
            ))

            result = await session.execute(query)
            return result.scalars().all()
