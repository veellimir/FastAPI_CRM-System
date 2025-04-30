from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.settings import Base
from core.mixins import IdIntPkMixin


class CategoryProduct(Base, IdIntPkMixin):
    __tablename__ = "category_product"

    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    products: Mapped[list["Product"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan"
    )


class Product(Base, IdIntPkMixin):
    __tablename__ = "product"

    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    descriptions: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(
        String(255),
        default="/static/default/none_product.png"
    )

    category_id: Mapped[int] = mapped_column(ForeignKey(
        "category_product.id"),
        nullable=False
    )
    category: Mapped["CategoryProduct"] = relationship(
        back_populates="products"
    )