from fastapi import HTTPException

EXCEPTION_CONFLICT_HTTP_400 = HTTPException(
    status_code=400,
    detail="Текущая роль уже существует"
)

EXCEPTION_ROLE_HTTP_404 = HTTPException(
    status_code=404,
    detail="Роль не найдена"
)
