from fastapi import APIRouter, UploadFile, File

from app.authentication.dependencies import fastapi_users
from app.authentication.dependencies import current_active_user, current_active_superuser

from app.products.schemas import CategoryProductReadSchem
from app.products.dao import CategoryProductDAO

from core.settings import settings

router = APIRouter(
    prefix=settings.api.v1.category_product,
    tags=["Категории товаров"]
)


# 🌐🔁 ──────────────── ROUTERS ──────────────── 🔁🌐

@router.get(
    "/get_list",
    summary="Получить список категорий товаров",
    response_model=list[CategoryProductReadSchem]
)
async def get_category() -> list[CategoryProductReadSchem]:
    return await CategoryProductDAO.find_all()
