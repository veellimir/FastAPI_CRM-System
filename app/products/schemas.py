from fastapi_users import schemas


class CategoryProductAddSchem(schemas.BaseModel):
    title: str


class CategoryProductReadSchem(schemas.BaseModel):
    id: int
    title: str
