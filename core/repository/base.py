from sqlalchemy import select

from core.settings.database import AsyncSessionLocal


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **kwargs):
        async with AsyncSessionLocal() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().all()

