from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from app.authentication.dependencies import current_active_superuser, current_active_user
from app.user import User

from app.role.dao import UserRoleDAO
from app.user.dao import UserDAO

from app.role.schemas import RoleAddSchem, RoleAssignAddSchem, RoleReadSchem

from core.settings.config import settings

from app.role.exceptions import EXCEPTION_ROLE_HTTP_404
from app.exceptions import EXCEPTION_USER_HTTP_404

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
    return await UserRoleDAO.add_role(title=role.title)


@router.post(
    "/assign",
    summary="Добавить роль пользователю",
    response_model=RoleAssignAddSchem
)
async def add_assign(
        data: RoleAssignAddSchem,
        user: User = Depends(current_active_user)
):
    user = await UserDAO.find_one(id=data.user_id)
    if not user:
        raise EXCEPTION_USER_HTTP_404

    role = await UserRoleDAO.find_one(id=data.role_id)
    if not role:
        raise EXCEPTION_ROLE_HTTP_404

    user.role_id = data.role_id
    await UserDAO.update(user)

    return RoleAssignAddSchem(user_id=data.user_id, role_id=data.role_id)


@router.get(
    "/get_list",
    summary="Получить список ролей",
    response_model=list[RoleReadSchem]
)
async def get_role(user: User = Depends(current_active_user)):
    return await UserRoleDAO.find_all()
