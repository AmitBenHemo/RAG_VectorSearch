from fastapi import FastAPI
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
from contextlib import asynccontextmanager
from pymongo.server_api import ServerApi
from fastapi.middleware.cors import CORSMiddleware

from apps.rag.routers import router as rag_router

#
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URI, server_api=ServerApi('1'))
    app.mongodb = app.mongodb_client.Evolink
    yield
    app.mongodb_client.close()
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rag_router, tags=["rags"], prefix="/rag")



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )