from core.repository import BaseDAO

from app.role import UserRole


class NewsDAO(BaseDAO):
    model = UserRole