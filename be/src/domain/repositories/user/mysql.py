from typing import List
from sqlalchemy import func

from sqlmodel import Session, select, or_

from src.app.dtos.user import GetUsersParams
from src.domain.entities.user import CreateUserEntity
from src.insfra.logger import LoggerFactory
from src.insfra.postgres import BasePostgres, UserModel

from .interface import UserRepositoryInterface


class UserPostgresRepository(BasePostgres[UserModel, CreateUserEntity], UserRepositoryInterface):
    def __init__(self):
        self.logger = LoggerFactory.get_logger()
        super().__init__(UserModel)

    def get_user_by_username(self, username: str) -> UserModel | None:
        try:
            with Session(self.engine) as session:
                query = select(self.model).where(
                    self.model.username == username)
                result = session.exec(query).first()
                return result

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def get_user_by_email(self, email: str) -> UserModel | None:
        try:
            with Session(self.engine) as session:
                query = select(self.model).where(self.model.email == email)
                result = session.exec(query).first()
                return result

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def get_users(self, params: GetUsersParams) -> List[UserModel] | None:
        try:
            with Session(self.engine) as session:
                query = select(self.model).offset(
                    params.offset).limit(params.limit)
                result = session.exec(query).all()

                users = [user for user in result]
                return users

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def count_total_users(self) -> int | None:
        try:
            with Session(self.engine) as session:
                query = select(func.count(self.model.id))
                result = session.exec(query).one()
                return result

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None
