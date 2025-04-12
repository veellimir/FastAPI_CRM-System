from fastapi import Depends

from app.authentication.user_manager import UserManager
from .user import get_users_db

from typing import Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
        users_db: Annotated[
            "SQLAlchemyUserDatabase",
            Depends(get_users_db),
        ]
):
    yield UserManager(users_db)
