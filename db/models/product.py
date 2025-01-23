from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, BigInteger, Index

from db.core import Base


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    artikul: Mapped[int] = mapped_column(BigInteger, unique=True)
    cost: Mapped[int] = mapped_column(BigInteger)
    rating: Mapped[float] = mapped_column(Float)
    total_quantity: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        Index("idx_products_article", "artikul"),
    )