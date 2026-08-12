from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.session import init_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title='База данных фильмов',
    description='API с данными от кино (TMBD, IMDb и.д)',
    version='1.0.0',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)