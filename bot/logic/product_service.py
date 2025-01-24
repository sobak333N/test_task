from typing import Optional, Any

from pydantic import ValidationError

from schemas import ProductSchema, ArtikulSchema
from errors import ProductDoesntExitstsExc, NotValidArtikulExc
from db.repositories import ProductRepository, AbsRepository
from db.core import get_session_manager


class ProductService:
    def __init__(
        self, product_repository: AbsRepository = ProductRepository(),
    ):
        self.product_repository = product_repository

    async def get_product(
        self, artikule: Any
    ) -> Optional[ProductSchema]:
        try:
            artikul_schema = ArtikulSchema(artikul=artikule)
        except ValidationError:
            raise NotValidArtikulExc()
        
        async with get_session_manager() as session:
            product = await self.product_repository.get_by_artikul(
                artikul_schema.artikul, session
            )
            if product:
                return ProductSchema.model_validate(product)
            raise ProductDoesntExitstsExc()
        