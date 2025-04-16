import logging

from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from core.settings import settings

from app.user import User

from .dependencies.smtp import send_email
from .dependencies.user import get_users_db

from typing import Optional, TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

# TODO: удалить логирование
log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
            self,
            user: User,
            request: Optional["Request"] = None,
    ):
        log.warning(
            "Пользователь %r зарегистрирован.",
            user.id,
        )

    async def on_after_request_verify(
            self,
            user: User,
            token: str,
            request: Optional["Request"] = None,
    ):
        log.warning('Для пользователя %r запрошена верификация: %r', user.id, token)

        verify_url = f"{settings.FRONTEND_URL}/verify?token={token}"
        await send_email(user.email, verify_url)

    async def on_after_forgot_password(
            self,
            user: User,
            token: str,
            request: Optional["Request"] = None,
    ):
        log.warning(
            "Пользователь %r забыл свой пароль. Токен сброса:%r",
            user.id,
            token,
        )


async def get_user_manager(
        users_db: Annotated[
            "SQLAlchemyUserDatabase",
            Depends(get_users_db),
        ]
):
    yield UserManager(users_db)
