from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from core.settings.database import get_async_session
from app.user import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(get_async_session),
    ],
):
    yield User.get_db(session=session)
