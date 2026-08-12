from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield