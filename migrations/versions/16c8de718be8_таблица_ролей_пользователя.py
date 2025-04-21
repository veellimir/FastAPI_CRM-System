"""Таблица ролей пользователя

Revision ID: 16c8de718be8
Revises: 5304a593627d
Create Date: 2025-04-21 16:02:01.128222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '16c8de718be8'
down_revision: Union[str, None] = '5304a593627d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('user_role',
    sa.Column('title', sa.String(length=100), nullable=False),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'user_role', ['role_id'], ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    op.drop_table('user_role')
