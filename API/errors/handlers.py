from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from .errors_list import (
    NotUniqueArtikulExc,  NotValidExternalDataExc,
    ProductDoesntExitstsExc, ServerErrorExc, AlreadySubscribedExc
)


async def not_unique_artikul_handler(
    request: Request, exc: NotUniqueArtikulExc
):
    return JSONResponse(
        status_code=400,
        content={"message": exc.detail},
    )


async def not_valid_external_data_handler(
    request: Request, exc: NotValidExternalDataExc
):
    return JSONResponse(
        status_code=400,
        content={"message": exc.detail},
    )


async def product_doesnt_exist_handler(
    request: Request, exc: ProductDoesntExitstsExc
):
    return JSONResponse(
        status_code=404,
        content={"message": exc.detail},
    )


async def server_error_handler(
    request: Request, exc: ServerErrorExc
):
    return JSONResponse(
        status_code=400,
        content={"message": exc.detail},
    )


async def already_subscribed_error_handler(
    request: Request, exc: AlreadySubscribedExc
):
    return JSONResponse(
        status_code=409,
        content={"message": exc.detail},
    )


def register_all_errors(fastapi: FastAPI):
    fastapi.add_exception_handler(
        NotUniqueArtikulExc, not_unique_artikul_handler
    )
    fastapi.add_exception_handler(
        NotValidExternalDataExc, not_valid_external_data_handler
    )
    fastapi.add_exception_handler(
        ProductDoesntExitstsExc, product_doesnt_exist_handler
    )
    fastapi.add_exception_handler(ServerErrorExc, server_error_handler)
    fastapi.add_exception_handler(
        AlreadySubscribedExc, already_subscribed_error_handler
    )

