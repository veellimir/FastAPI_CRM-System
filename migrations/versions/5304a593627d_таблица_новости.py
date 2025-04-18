"""Таблица новости

Revision ID: 5304a593627d
Revises: 799f2e744280
Create Date: 2025-04-18 15:56:01.522169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '5304a593627d'
down_revision: Union[str, None] = '799f2e744280'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'news',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                sa.Column('title', sa.String(length=100), nullable=False),
                sa.Column('descriptions', sa.String(length=255), nullable=True),
                sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('news')
