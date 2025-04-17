from pydantic import Field
from fastapi_users import schemas


class UserCreate(schemas.BaseUserCreate):
    pass


class UserRead(schemas.BaseUser[int]):
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    image: str | None = Field(default=None)


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
