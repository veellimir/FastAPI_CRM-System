from app.news import News

from core.settings.database import AsyncSessionLocal
from core.repository import BaseDAO


class NewsDAO(BaseDAO):
    model = News

    @classmethod
    async def add(cls, title, description):
        async with AsyncSessionLocal() as session:
            obj = cls.model(title=title, descriptions=description)
            session.add(obj)
            await session.commit()
            return obj

