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

    @classmethod
    async def find_one(cls, **kwargs):
        async with AsyncSessionLocal() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().first()

    @classmethod
    async def add(cls, **kwargs):
        async with AsyncSessionLocal() as session:
            obj = cls.model(**kwargs)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    @classmethod
    async def update(cls, instance):
        async with AsyncSessionLocal() as session:
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance