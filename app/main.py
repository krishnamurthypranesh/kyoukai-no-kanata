from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.connectors import db_session_factory
from app import database
from app.routers import OpsRouter

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


_engine, _sessionmaker = db_session_factory()
database.engine = _engine
database.SessionLocal = _sessionmaker


app.include_router(OpsRouter)

