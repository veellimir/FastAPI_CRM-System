from fastapi_users import FastAPIUsers

from app.authentication.user_manager import get_user_manager
from app.authentication.dependencies.backend import authentication_backend
from app.authentication.dependencies.services import send_email

from app.user import User
from app.user.schemas import UserRead, UserCreate

from core.settings import settings


async def on_after_register(user: User, request=None) -> None:
    token = await fastapi_users.verification_token_strategy.write_token(user)
    verify_url = f"{settings.FRONTEND_URL}/verify?{token}"
    send_email(user.email, verify_url)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
    UserRead,
    UserCreate,
    User,
    after_register=on_after_register
)