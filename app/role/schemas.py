from fastapi_users import schemas


class UserRoleCreate(schemas.BaseModel):
    title: str


class RoleAssign(schemas.BaseModel):
    user_id: int
    role_id: int


class UserRoleRead(schemas.BaseModel):
    title: str
