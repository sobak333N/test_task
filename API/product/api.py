from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp import ClientSession

from db.core import get_session
from schemas import ProductPostRequestSchema, ProductSchema
from depends import get_http_session
from .data_fetcher import HttpFetcher
from .service import ProductService


product_router = APIRouter()
http_fetcher = HttpFetcher()
product_service = ProductService()


@product_router.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
async def post_products(
    product_data: ProductPostRequestSchema,
    session: AsyncSession = Depends(get_session),
    http_session: ClientSession = Depends(get_http_session)
):
    external_product_model = await http_fetcher.fetch_data(
        http_session, product_data.articule
    )
    return await product_service.create(external_product_model, session)
    # print(product_data)
    # print(session)
    # print(http_session)
    # ...
