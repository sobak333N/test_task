from typing import Any
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp import ClientSession
from fastapi import Depends
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from errors import AlreadySubscribedExc
from .data_fetcher import HttpFetcher
from abstracts import AbsService, AbsDataFetcher
from schemas import ProductExternalSchena, ProductSchema
from db.repositories import ProductRepository, AbsRepository
from db.core import get_session_manager
from depends import get_http_session


class ProductService(AbsService):
    def __init__(
        self, 
        product_repository: AbsRepository = ProductRepository(),
        data_fetcher: AbsDataFetcher = HttpFetcher()
    ):
        self.product_repository = product_repository
        self.data_fetcher = data_fetcher

    async def create(
        self, model: ProductExternalSchena, session: AsyncSession
    ) -> ProductSchema:
        product = await self.product_repository.get_by_artikul(
            model.artikul, session
        )
        if product:
            return ProductSchema.model_validate(product)
        # some another business logic
        return await self.product_repository.create(model, session)
    
    async def subscribe(self, artikul: int, scheduler: AsyncIOScheduler):
        job_id = f"fetch_product_{artikul}"

        if scheduler.get_job(job_id):
            raise AlreadySubscribedExc()
    
        scheduler.add_job(
            self.regular_task,
            trigger='interval',
            minutes=30,
            args=[artikul],
            id=job_id,
            replace_existing=False,
        )

    async def regular_task(self, pk: int) -> None:
        async def task():
            async with ClientSession() as http_session:
                external_product_model = await self.fetch_data(
                    pk, http_session
                )
            async with get_session_manager() as session:
                await self.update(pk, external_product_model, session)
        asyncio.create_task(task())

    async def update(
        self, pk: int, model: ProductExternalSchena, session: AsyncSession
    ) -> ProductSchema:
        product = await self.product_repository.get_by_artikul(
            model.artikul, session
        )
        if not product:
            return await self.create(model, session)
        return await self.product_repository.update(product, model, session)

    async def fetch_data(
        self, pk: int, session: Any
    ) -> ProductExternalSchena:
        return await self.data_fetcher.fetch_data(pk, session)
