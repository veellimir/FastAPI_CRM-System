from fastapi import APIRouter, UploadFile, File
from fastapi.params import Depends, Query

from app.authentication.dependencies import fastapi_users
from app.authentication.dependencies import current_active_user, current_active_superuser

from app.user import User

from app.user.schemas import UserRead, UserUpdate
from app.user.upload_image import upload_avatar

from core.settings import settings
from app.user.dao import UserDAO


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


# @router.get(
#     "/search",
#     summary="Поиск по подстроке",
#     response_model=list[UserRead]
# )
# async def search_users(
#         query: str = Query(..., min_length=1),
#         current_user: User = Depends(current_active_user)
# ):
#     print(f"🔑 Пользователь: {current_user.email}")
#     users = await UserDAO.search(query)
#     return [
#         UserRead(
#             id=user.id,
#             first_name=user.first_name,
#             last_name=user.last_name,
#             email=user.email
#         )
#         for user in users ]