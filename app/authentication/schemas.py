from pydantic import BaseModel


class UserLoginRequest(BaseModel):
    email: str


class UserResponse(BaseModel):
    message: str
    user: str
