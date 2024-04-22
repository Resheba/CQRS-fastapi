from fastapi import FastAPI

from src.app.routers import UserRouter


def app() -> FastAPI:
    app = FastAPI()
    app.include_router(UserRouter)
    return app
