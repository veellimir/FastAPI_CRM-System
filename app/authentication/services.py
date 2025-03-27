import jwt

from datetime import datetime, timedelta

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from settings.config import settings

from .models import User
from .utils import send_email


def generate_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


async def request_login(email: str, session: AsyncSession):
    result = await session.execute(select(User).where(User.email == email))
    user = result.scalars().first()

    if not user:
        user = User(email=email)
        session.add(user)
        await session.commit()

    token = generate_token(email)

    await send_email(email, token)
    return {"message": "Ссылка для входа отправлена на email", "user": user.email}


async def login(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return {
            "message": "Успешный вход",
            "user": payload["sub"]
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Токен истёк")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Неверный токен")
