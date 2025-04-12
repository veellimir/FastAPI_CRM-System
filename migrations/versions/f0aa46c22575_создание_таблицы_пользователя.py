"""создание таблицы пользователя

Revision ID: f0aa46c22575
Revises: 
Create Date: 2025-04-10 20:25:45.917039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'f0aa46c22575'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('email', sa.String(length=320), nullable=False),
            sa.Column('hashed_password', sa.String(length=1024), nullable=False),
            sa.Column('is_active', sa.Boolean(), nullable=False),
            sa.Column('is_superuser', sa.Boolean(), nullable=False),
            sa.Column('is_verified', sa.Boolean(), nullable=False),
            sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
