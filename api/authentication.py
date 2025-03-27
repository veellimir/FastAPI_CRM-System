from fastapi import APIRouter

from app.authentication.routers import router as auth_router
from settings.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
    tags=["Authentication user"]
)
router.include_router(auth_router)
