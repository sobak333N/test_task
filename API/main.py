from fastapi import FastAPI

from product.api import product_router
from errors.handlers import register_all_errors 

version = "1.0.0"  # Установите корректный формат версии
version_prefix = f"/api/v1"  # Это будет использоваться в URL

description = """
REST API для получения информации о продуктах и подписки на обновления.

Функционал API включает:
- Получение подробной информации о продукте по артикулу
- Подписку на обновления данных о продукте
"""

app = FastAPI(
    title="Трекер Продуктов API",
    description=description,
    version=version,  # Версия в правильном формате
    contact={
        "name": "Рязанский Вячеслав",
        "url": "https://github.com/sobak333N",
        "email": "p.ko1@yandex.com",
    },
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)
app.include_router(
    product_router, prefix=version_prefix, tags=["products"]
)
