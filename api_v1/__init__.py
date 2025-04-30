from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.settings import settings

from .authentication import router as auth_router
from .user import router as users_router
from .user_role import router as role_router
from .news import router as news_router
from .notification import router as notification_router
from .category_product import  router as category_products

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(auth_router)
router.include_router(users_router)
router.include_router(role_router)
router.include_router(news_router)
router.include_router(notification_router)
router.include_router(category_products)