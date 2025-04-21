from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File
from fastapi.params import Depends

from app.authentication.dependencies import fastapi_users
from app.authentication.dependencies import current_active_user

from app.user import User

from app.user.schemas import UserRead, UserUpdate
from app.user.upload_image import upload_avatar

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

@router.put("/avatar")
async def upload_image(
        file: UploadFile = File(...),
        current_user: User = Depends(current_active_user)
):
    return await upload_avatar(current_user.id, file)
