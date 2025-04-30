from fastapi import HTTPException, status

from fastapi import APIRouter, UploadFile, File
from sqlalchemy.exc import IntegrityError

from app.authentication.dependencies import fastapi_users
from app.authentication.dependencies import current_active_user, current_active_superuser

from app.products.exceptions import EXCEPTION_CONFLICT_HTTP_409

from app.products.schemas import CategoryProductAddSchem, CategoryProductReadSchem
from app.products.dao import CategoryProductDAO

from core.settings import settings

router = APIRouter(
    prefix=settings.api.v1.category_product,
    tags=["Категории товаров"]
)


# 🌐🔁 ──────────────── ROUTERS ──────────────── 🔁🌐

@router.post(
    "/add",
    summary="Добавить категорию товара",
    response_model=CategoryProductAddSchem
)
async def add_category(title: str):
    try:
        return await CategoryProductDAO.add(title=title)
    except IntegrityError as e:
        if 'category_product_title_key' in str(e):
            raise EXCEPTION_CONFLICT_HTTP_409


@router.get(
    "/get_list",
    summary="Получить список категорий товаров",
    response_model=list[CategoryProductReadSchem]
)
async def get_category() -> list[CategoryProductReadSchem]:
    return await CategoryProductDAO.find_all()
