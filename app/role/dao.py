from core.repository import BaseDAO

from app.role import UserRole


class UserRoleDAO(BaseDAO):
    model = UserRole