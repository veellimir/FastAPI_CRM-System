from fastapi import APIRouter

from app.authentication.dependencies.fastapi_users import fastapi_users
from app.user.schemas import UserRead, UserUpdate
from core.settings.config import settings

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Пользователи"]
)


# 🌐🔁 ──────────────── ROUTERS ──────────────── 🔁🌐

router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)