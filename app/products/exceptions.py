from fastapi import HTTPException

EXCEPTION_CONFLICT_HTTP_409 = HTTPException(
    status_code=409,
    detail="Категория с таким названием уже существует"
)
