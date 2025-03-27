from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.authentication.schemas import UserLoginRequest, UserResponse
from app.authentication.services import request_login, login

from settings.database import get_async_session
from settings.config import settings

router = APIRouter(prefix=settings.api.v1.auth)


@router.post("/request_email", response_model=UserResponse)
async def request_login_route(data: UserLoginRequest, session: AsyncSession = Depends(get_async_session)):
    result = await request_login(data.email, session)
    return {"message": result["message"], "user": result["user"]}


@router.post("/login", response_model=UserResponse)
async def login_route(token: str):
    return await login(token)
