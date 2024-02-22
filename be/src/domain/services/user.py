from typing import List

from src.app.dtos.user import UserResponse, CreateUserParams, GetUsersParams
from src.common.crypto_helper import CryptoHelper
from src.common.singleton import SingletonMeta
from src.domain.entities.user import CreateUserEntity
from src.domain.repositories.user.interface import UserRepositoryInterface
from src.domain.repositories.user.mysql import UserPostgresRepository
from src.insfra.logger import LoggerFactory


class UserServices(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = LoggerFactory.get_logger()
        self.user_repos: UserRepositoryInterface = UserPostgresRepository()

    def create_user(self, params: CreateUserParams) -> UserResponse | None:
        try:
            salt = CryptoHelper.gen_salt()
            hashed_password = CryptoHelper.hash_password(params.password, salt)
            entity = CreateUserEntity(
                email=params.email,
                username=params.username,
                hashed_password=hashed_password,
                salt=salt,
                fullname=params.fullname
            )

            model = self.user_repos.create(entity)
            data = UserResponse.from_model(model)
            return data
        except Exception as e:
            self.logger.log_error(e.__str__())
            return None

    def get_user_by_username(self, username: str) -> UserResponse | None:
        try:
            model = self.user_repos.get_user_by_username(username)
            if model is None:
                return None

            data = UserResponse.from_model(model)
            return data
        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def get_users(self, params: GetUsersParams) -> List[UserResponse] | None:
        try:
            user_models = self.user_repos.get_users(params)
            if user_models is None:
                return None

            user_res = [UserResponse.from_model(user_model) for user_model in user_models]
            return user_res
        except Exception as e:
            self.logger.log_error(e.__str__())

        return None
