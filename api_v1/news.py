from typing import Optional

from fastapi import APIRouter, Depends

from app.authentication.dependencies.fastapi_users import current_active_user
from app.user import User

from app.news.dao import NewsDAO
from app.news.schemas import NewsAddSchem, NewsReadSchem

from core.settings import settings
from .notification import send_notification

router = APIRouter(
    prefix=settings.api.v1.news,
    tags=["Новостная лента"]
)


# 🌐🔁 ──────────────── ROUTERS ──────────────── 🔁🌐

@router.post(
    "/add",
    summary="Добавить новость",
    response_model=NewsAddSchem
)
async def add_news(
        title: str,
        description: Optional[str] = None,
        user: User = Depends(current_active_user)
):
    return await NewsDAO.add(title=title, description=description)


@router.get(
    "/get_list",
    summary="Получить список новостей",
    response_model=list[NewsReadSchem]
)
async def get_news(user: User = Depends(current_active_user)):
    # await send_notification("кто-то получил сообщение новостей")
    return await NewsDAO.find_all()
