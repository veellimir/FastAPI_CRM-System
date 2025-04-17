from fastapi import APIRouter, UploadFile, File
from fastapi.params import Depends

from app.authentication.dependencies.fastapi_users import fastapi_users

from app.user.schemas import UserRead, UserUpdate
from app.user.upload_image import upload_avatar

from core.settings.config import settings
from core.settings.database import get_async_session

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

@router.put("/avatar/{user_id}", dependencies=[Depends(get_async_session)])
async def upload_image(user_id: int, file: UploadFile = File(...)):
    return await upload_avatar(user_id, file)
