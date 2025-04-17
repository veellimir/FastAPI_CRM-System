from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.settings import Base
from core.mixins import IdIntPkMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    first_name: Mapped[str | None] = mapped_column(String(length=100))
    last_name: Mapped[str | None] = mapped_column(String(length=100))
    image: Mapped[str | None] = mapped_column(String(255))

    @classmethod
    def get_db(cls, session: "AsyncSession"):  # Брать для получения этого объекта
        return SQLAlchemyUserDatabase(session, cls)
