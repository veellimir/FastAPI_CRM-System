from fastapi import Depends

from fastapi_users.authentication.strategy.db import DatabaseStrategy

from core.settings import settings
from .access_token import get_access_tokens_db

from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from app.authentication.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
        access_tokens_db: Annotated[
            "AccessTokenDatabase[AccessToken]",
            Depends(get_access_tokens_db),
        ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
