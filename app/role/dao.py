from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from core.settings.database import AsyncSessionLocal
from core.repository import BaseDAO

from app.role import UserRole

from .exceptions import EXCEPTION_CONFLICT_HTTP_400


class UserRoleDAO(BaseDAO):
    model = UserRole

    @classmethod
    async def add_role(cls, **kwargs):
        async with AsyncSessionLocal() as session:
            obj = cls.model(**kwargs)
            session.add(obj)
            try:
                await session.commit()
                await session.refresh(obj)
                return obj
            except IntegrityError:
                raise EXCEPTION_CONFLICT_HTTP_400

    @classmethod
    async def search(cls, substring: str):
        async with AsyncSessionLocal() as session:
            query = select(cls.model).where(cls.model.title.ilike(f"%{substring}%"))
            result = await session.execute(query)
            return result.scalars().all()