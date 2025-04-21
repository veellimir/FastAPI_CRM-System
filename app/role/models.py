from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from core.settings import Base
from core.mixins import IdIntPkMixin


class UserRole(Base, IdIntPkMixin):
    __tablename__ = "user_role"

    title: Mapped[str] = mapped_column(String(100), nullable=False)