from fastapi import APIRouter, Depends

from app.authentication.dependencies.fastapi_users import (
    current_active_user,
    current_active_superuser
)

from app.user import User
from app.user.schemas import UserRead

from core.settings import settings

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Сообщения"]
)


@router.get("", summary="Получить сообщение для пользователя")
def get_user_messages(user: User = Depends(current_active_user)):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user)
    }


@router.get("/secrets", summary="Получить сообщение для администратора")
def get_superuser_messages(user: User = Depends(current_active_superuser)):
    return {
        "messages": ["secret-m1", "secret-m2", "secret-m3"],
        "user": UserRead.model_validate(user)
    }
