from core.repository import BaseDAO

from .models import CategoryProduct


class CategoryProductDAO(BaseDAO):
    model = CategoryProduct