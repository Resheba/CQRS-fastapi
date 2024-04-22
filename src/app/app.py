from fastapi import FastAPI

from src.app.routers import UserRouter
from src.app.core.exception import BaseHTTPException

from src.infrastructure.setup import setup_mediator


def app() -> FastAPI:
    app = FastAPI(
        title='CQRS Mediator FastAPI example',
        exception_handlers={
            BaseHTTPException: BaseHTTPException.handler
        }
    )
    setup_mediator()
    app.include_router(UserRouter)
    return app
