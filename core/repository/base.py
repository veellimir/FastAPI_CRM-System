from sqlalchemy import select, insert

from core.settings.database import get_async_session

class BaseDAO:
    model = None

