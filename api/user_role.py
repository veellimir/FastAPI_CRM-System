from fastapi import APIRouter
from fastapi.params import Depends

from app.authentication.dependencies import current_active_superuser, current_active_user
from app.user import User

from app.role.dao import UserRoleDAO
from app.role.schemas import RoleAddSchem, RoleReadSchem

from core.settings.config import settings

router = APIRouter(
    prefix=settings.api.v1.role,
    tags=["Роль Пользователей"]
)


# 🌐🔁 ──────────────── ROUTERS ──────────────── 🔁🌐

@router.post(
    "/add",
    summary="Создать роль пользователя",
    response_model=RoleAddSchem
)
async def create_role(role: RoleAddSchem, user: User = Depends(current_active_superuser)):
    return await UserRoleDAO.add(title=role.title)

@router.get(
    "/get_list",
    summary="Получить список ролей",
    response_model=list[RoleAddSchem]
)
async def get_role(user: User = Depends(current_active_user)):
    return await UserRoleDAO.find_all()