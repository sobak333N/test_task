from fastapi import FastAPI

from product.api import product_router
from errors.handlers import register_all_errors 


version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix = f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Ryazanskii Vyacheslav",
        "url": "https://github.com/sobak333N",
        "email": "p.ko1@yandex.com",
    },
    terms_of_service="httpS://example.com/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)
app.include_router(
    product_router, prefix=f"{version_prefix}/products", tags=["products"]
)
