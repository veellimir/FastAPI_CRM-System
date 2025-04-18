from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from core.settings import Base
from core.mixins import IdIntPkMixin


class News(Base, IdIntPkMixin):
    __tablename__ = "news"

    title: Mapped[str] = mapped_column(
        String(length=100),
        nullable=False
    )
    descriptions: Mapped[str | None] = mapped_column(
        String(length=255),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
