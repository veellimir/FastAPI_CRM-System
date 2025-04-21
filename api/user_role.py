from fastapi import APIRouter
from fastapi.params import Depends

from app.role.dao import UserRoleDAO
from app.role.schemas import RoleAddSchem

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
async def create_role(role: RoleAddSchem):
    return await UserRoleDAO.add(title=role.title)
