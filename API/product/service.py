from sqlalchemy.ext.asyncio import AsyncSession

from abstracts import AbsService
from schemas import ProductExternalSchena, ProductSchema
from db.repositories import ProductRepository


class ProductService(AbsService):
    def __init__(
        self, product_repository: ProductRepository = ProductRepository()
    ):
        self.product_repository = product_repository

    async def create(
        self, model: ProductExternalSchena, session: AsyncSession
    ) -> ProductSchema:
        product = await self.product_repository.get_by_articule(
            model.articule, session
        )
        if product:
            return ProductSchema.model_validate(product)
        # some another business logic
        return await self.product_repository.create(model, session)
    
    async def update(self, pk, model, session):
        ...