from fastapi import APIRouter

from app.authentication.dependencies.backend import authentication_backend
from app.authentication.dependencies.fastapi_users import fastapi_users

from app.user.schemas import UserRead, UserCreate

from core.settings.config import settings

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Аутентификация"]
)


# 🌐🔁 ──────────────── ROUTERS ──────────────── 🔁🌐

router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        # requires_verification=True, вход только подтвержденных польз-тей
    ),
    responses={401: {"description": "Неверный логин или пароль"}},
)

router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

router.include_router(
    router=fastapi_users.get_verify_router(UserRead)
)

router.include_router(
    router=fastapi_users.get_reset_password_router()
)