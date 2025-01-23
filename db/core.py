from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine, AsyncSession, create_async_engine
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import Config


class Base(DeclarativeBase):
    pass


print(Config.DATABASE_URL)
engine: AsyncEngine = create_async_engine(
    Config.DATABASE_URL,
    echo=True,
)

sync_engine: Engine = create_engine(
    Config.SYNC_DATABASE_URL,
    echo=True
)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@asynccontextmanager
async def get_session_manager() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session