"""создание таблицы access token

Revision ID: 01e35ac2cb99
Revises: f0aa46c22575
Create Date: 2025-04-10 21:01:56.175436

"""
from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


revision: str = '01e35ac2cb99'
down_revision: Union[str, None] = 'f0aa46c22575'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('accesstoken',
    sa.Column('user_id', sa.Integer(), nullable=False),
            sa.Column('token', sa.String(length=43), nullable=False),
            sa.Column('created_at', fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True), nullable=False),
            sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='cascade'),
            sa.PrimaryKeyConstraint('token')
    )
    op.create_index(op.f('ix_accesstoken_created_at'), 'accesstoken', ['created_at'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_accesstoken_created_at'), table_name='accesstoken')
    op.drop_table('accesstoken')
