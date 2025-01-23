from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .abstract_repository import AbsRepository
from db.models import Product
from schemas import ProductExternalSchena, ProductSchema


class ProductRepository(AbsRepository):
    async def get(self, pk: int, session: AsyncSession) -> ProductSchema:
        pass

    async def get_by_artikul(
        self, artikul: int, session: AsyncSession
    ) -> Optional[ProductSchema]:
        statement = (
            select(Product)
            .where(Product.artikul == artikul)
        )
        result = await session.execute(statement)
        return result.scalar_one_or_none()

    async def create(
        self, model: ProductExternalSchena, session: AsyncSession
    ) -> ProductSchema:
        product = Product(**model.model_dump())
        session.add(product)
        await session.commit()
        return ProductSchema.model_validate(product)

    async def delete(self, pk: int, session: AsyncSession) -> None:
        pass

    async def update(
        self, instance: Product, 
        model: ProductExternalSchena, session: AsyncSession
    ) -> ProductSchema:
        model_data = model.model_dump(exclude_unset=True)
        for attr, value in model_data.items():
            setattr(instance, attr, value)
        session.add(instance)
        await session.commit()
        await session.refresh(instance)
        return ProductSchema.model_validate(instance)
