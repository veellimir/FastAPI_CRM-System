from fastapi import HTTPException

EXCEPTION_IMAGE_HTTP_500 = HTTPException(
    status_code=500,
    detail="Ошибка загрузки изображения"
)

EXCEPTION_USER_HTTP_404 = ValueError("Некорректный выбранный пользователь")