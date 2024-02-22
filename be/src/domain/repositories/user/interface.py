from abc import ABC, abstractmethod
from typing import List

from src.app.dtos.user import GetUsersParams
from src.domain.entities.user import CreateUserEntity
from src.insfra.postgres import BasePostgresInterface, UserModel


class UserRepositoryInterface(BasePostgresInterface[UserModel, CreateUserEntity], ABC):
    @abstractmethod
    def get_user_by_username(self, username: str) -> UserModel | None:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserModel | None:
        pass

    @abstractmethod
    def get_users(self, params: GetUsersParams) -> List[UserModel] | None:
        pass
