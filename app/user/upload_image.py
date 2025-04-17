from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile, File
from starlette.responses import JSONResponse

from app.exceptions import EXCEPTION_IMAGE_HTTP_500
from app.user.dao import UserDAO

from core.settings import settings


async def upload_avatar(user_id: int, file: UploadFile = File(...)):
    try:
        extension = file.filename.split('.')[-1]
        new_filename = f"{uuid4()}.{extension}"

        image_dir = Path(settings.media.MEDIA_FOLDER_PROFILE)
        if not image_dir.exists():
            image_dir.mkdir(parents=True)

        with open(image_dir / new_filename, "wb") as buffer:
            buffer.write(await file.read())

        await UserDAO.update_user_avatar(user_id, new_filename)
        return JSONResponse(content={"message": "Изображение обновлено"})
    except Exception:
        return EXCEPTION_IMAGE_HTTP_500

