from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .env_config import DATABASE_URL

SECRET = "SECRET"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# __all__ = ["Base", "engine", "AsyncSessionLocal", "get_async_session"]