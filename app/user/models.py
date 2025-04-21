from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.settings import Base
from core.mixins import IdIntPkMixin

from app.role.models import UserRole

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    first_name: Mapped[str | None] = mapped_column(String(length=100))
    last_name: Mapped[str | None] = mapped_column(String(length=100))
    image: Mapped[str | None] = mapped_column(String(255))

    role_id: Mapped[int] = mapped_column(ForeignKey("user_role.id"), nullable=True)
    role: Mapped["UserRole"] = relationship("UserRole", backref="user")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
