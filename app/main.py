from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.infra.db.database import Database
from app.models.settings import Settings
from app.routes.router import router

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Database.init(
        settings.DB_URI,
    )
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        reload=True,
    )
