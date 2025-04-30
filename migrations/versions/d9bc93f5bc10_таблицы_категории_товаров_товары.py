"""таблицы: категории товаров, товары

Revision ID: d9bc93f5bc10
Revises: 9be2213fc9a7
Create Date: 2025-04-30 22:07:26.214187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd9bc93f5bc10'
down_revision: Union[str, None] = '9be2213fc9a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('category_product',
    sa.Column('title', sa.String(length=100), nullable=False),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('title')
    )
    op.create_table('product',
    sa.Column('title', sa.String(length=100), nullable=False),
                sa.Column('descriptions', sa.Text(), nullable=False),
                sa.Column('image', sa.String(length=255), nullable=False),
                sa.Column('category_id', sa.Integer(), nullable=False),
                sa.Column('id', sa.Integer(), nullable=False),
                sa.ForeignKeyConstraint(['category_id'], ['category_product.id'], ),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('title')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('product')
    op.drop_table('category_product')
