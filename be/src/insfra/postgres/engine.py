from sqlalchemy import Engine
from sqlmodel import create_engine, SQLModel
from src.common import Config
from src.common.singleton import SingletonMeta


class PostgresEngine(metaclass=SingletonMeta):
    def __init__(self, config: Config) -> None:
        self.engine = create_engine(config.get_postgres_url(), echo=True)
        SQLModel.metadata.create_all(self.engine)

    def get_engine(self) -> Engine:
        return self.engine


