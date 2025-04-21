"""Обновление Таблицы ролей, уникальная роль

Revision ID: 9be2213fc9a7
Revises: 16c8de718be8
Create Date: 2025-04-21 16:40:17

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '9be2213fc9a7'
down_revision: Union[str, None] = '16c8de718be8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(None, 'user_role', ['title'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'user_role', type_='unique')
