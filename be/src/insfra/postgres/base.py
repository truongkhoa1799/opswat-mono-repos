from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Type, TypeVar,  Optional

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlmodel import Session

from src.common import Config
from src.insfra.logger import LoggerFactory
from src.insfra.postgres.engine import PostgresEngine

Model = TypeVar("Model", bound=Any)
CreateEntity = TypeVar("CreateEntity", bound=BaseModel)


class BasePostgresInterface(ABC, Generic[Model, CreateEntity]):
    @abstractmethod
    def get(self, id: Any) -> Optional[Model]:
        pass

    @abstractmethod
    def create(self, obj_in: CreateEntity) -> Model:
        pass

    @abstractmethod
    def update(self, db_obj: Model, obj_in: Dict[str, Any]) -> Model:
        pass

    @abstractmethod
    def remove(self, id: int) -> None:
        pass


class BasePostgres(BasePostgresInterface, Generic[Model, CreateEntity]):
    def __init__(self, model: Type[Model]):
        self.model = model
        self.config = Config()
        self.logger = LoggerFactory.get_logger()
        self.engine = PostgresEngine(self.config).get_engine()

    def get(self, id: Any) -> Optional[Model]:
        with Session(self.engine) as session:
            query = session.query(self.model).filter(self.model.id == id)
            result = query.first()
            return result

    def create(self, obj_in: CreateEntity) -> Model:
        with Session(self.engine) as session:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data)  # type: ignore
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def update(
            self,
            db_obj: Model,
            obj_in: Dict[str, Any]
    ) -> Model:
        with Session(self.engine) as session:
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.model_dump(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def remove(self, id: int) -> None:
        with Session(self.engine) as session:
            obj = session.query(self.model).get(id)
            session.delete(obj)
            session.commit()
            return
