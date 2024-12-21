import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from api.api_router import api_router

from db.init_db import init_models

from db.session import validation_client


@asynccontextmanager
async def lifespan(_):
    # On startup
    await init_models()
    validation_client.configure(asyncio.get_running_loop())
    await validation_client.connect()

    yield

    # On shutdown
    pass

app = FastAPI(
    lifespan=lifespan
)
app.include_router(api_router, prefix="/api/v1")


if __name__ == '__main__':
    uvicorn.run('main:app',
                host=settings.SERVER_HOST,
                port=settings.SERVER_PORT)
