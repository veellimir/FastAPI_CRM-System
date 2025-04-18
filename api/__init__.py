from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.settings import settings

from .authentication import router as auth_router
from .user import router as users_router
from .messages import router as messages_router
from .news import router as news_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(auth_router)
router.include_router(users_router)
router.include_router(messages_router)
router.include_router(news_router)