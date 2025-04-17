"""Добавление новых полей для пользователя

Revision ID: 799f2e744280
Revises: 01e35ac2cb99
Create Date: 2025-04-16 19:19:06.724348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '799f2e744280'
down_revision: Union[str, None] = '01e35ac2cb99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('user', sa.Column('first_name', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('image', sa.String(length=255), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('user', 'image')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
