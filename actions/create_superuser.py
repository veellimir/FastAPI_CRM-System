import asyncio
import contextlib

from app.authentication.user_manager import get_user_manager
from app.authentication.dependencies.user import get_users_db
from app.authentication.user_manager import UserManager

from app.user.schemas import UserCreate
from app.user.models import User

from core.settings.database import get_async_session

from core.settings.env_config import (
    SUPER_USER_EMAIL,
    SUPER_USER_PASSWORD,
    SUPER_USER_IS_ACTIVE,
    SUPER_USER_IS_SUPERUSER,
    SUPER_USER_IS_VERIFIED
)

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(user_manager: UserManager, user_create: UserCreate) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
        email: str = SUPER_USER_EMAIL,
        password: str = SUPER_USER_PASSWORD,
        is_active: bool = SUPER_USER_IS_ACTIVE,
        is_superuser: bool = SUPER_USER_IS_SUPERUSER,
        is_verified: bool = SUPER_USER_IS_VERIFIED
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with get_async_session_context() as session:
        async with get_users_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
