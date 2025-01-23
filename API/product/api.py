from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp import ClientSession

from db.core import get_session
from schemas import ProductPostRequestSchema, ProductSchema
from depends import get_http_session
from .service import ProductService
from scheduler import scheduler


product_router = APIRouter()
product_service = ProductService()


@product_router.post("/product", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
async def post_products(
    product_data: ProductPostRequestSchema,
    session: AsyncSession = Depends(get_session),
    http_session: ClientSession = Depends(get_http_session)
):
    external_product_model = await product_service.fetch_data(
        product_data.artikul, http_session
    )
    return await product_service.create(external_product_model, session)


@product_router.get("/subscribe/{artikul}", status_code=status.HTTP_200_OK)
async def get_subscribe(
    artikul: int,
):
    await product_service.subscribe(artikul, scheduler)