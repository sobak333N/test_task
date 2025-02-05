from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp import ClientSession

from db.core import get_session
from schemas import ArtikulSchema, ProductSchema
from depends import get_http_session
from .service import ProductService
from scheduler import scheduler
from auth import TokenDepends

product_router = APIRouter()
product_service = ProductService()


@product_router.post("/product", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
async def post_products(
    product_data: ArtikulSchema,
    session: AsyncSession = Depends(get_session),
    http_session: ClientSession = Depends(get_http_session),
    token: str = Depends(TokenDepends()),
):
    external_product_model = await product_service.fetch_data(
        product_data.artikul, http_session
    )
    return await product_service.create(external_product_model, session)


@product_router.get("/subscribe/{artikul}", status_code=status.HTTP_200_OK)
async def get_subscribe(
    artikul: int,
    token: str = Depends(TokenDepends()),
):
    await product_service.subscribe(artikul, scheduler)
    return JSONResponse(
        status_code=200,
        content={"message": f"Подписка на товар артикула {artikul} успешно оформлена"},
    )
