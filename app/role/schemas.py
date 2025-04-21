from fastapi_users import schemas


class RoleAddSchem(schemas.BaseModel):
    title: str


class RoleAssignAddSchem(schemas.BaseModel):
    user_id: int
    role_id: int


class RoleReadSchem(schemas.BaseModel):
    title: str
