from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.infra.db.database import Database
from app.models.settings import Settings

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Database.init(
        settings.DB_URI,
    )
    yield


app = FastAPI(lifespan=lifespan)
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        reload=True,
    )
