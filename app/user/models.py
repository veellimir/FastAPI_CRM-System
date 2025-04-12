from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.settings import Base
from core.mixins import IdIntPkMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    # TODO: Добавить нужные поля

    @classmethod
    def get_db(cls, session: "AsyncSession"):  # Брать для получения этого объекта
        return SQLAlchemyUserDatabase(session, cls)
