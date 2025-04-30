from fastapi_users import schemas


class CategoryProductAddSchem(schemas.BaseModel):
    title: str


class CategoryProductReadSchem(schemas.BaseModel):
    category_id: int
    title: str
