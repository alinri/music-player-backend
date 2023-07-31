from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

"""Mount upload files"""
app.mount(
    "/upload",
    StaticFiles(directory="app/upload"),
    name="upload",
)

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        reload=True,
    )
