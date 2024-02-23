from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.controllers import api_router
from src.app.middlewares.auth import AuthMiddleware
from src.app.middlewares.recover import RecoverMiddleware
from src.common import Config
from src.insfra.postgres.engine import PostgresEngine

app = FastAPI()
config = Config()
mysql_engine = PostgresEngine(config)


# ------------- Init Middlewares -------------
app.add_middleware(AuthMiddleware)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RecoverMiddleware)

# ------------- Init routes -------------
app.include_router(api_router)
