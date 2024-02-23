from datetime import timedelta
from typing import Any, Dict

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from src.app.presenters.user import UserPresenter

from src.app.controllers.base import BaseController
from src.app.presenters.auth import AuthPresenter
from src.app.presenters.base import BasePresenter
from src.common import Config
from src.common.crypto_helper import CryptoHelper
from src.common.messages import UserErrMsg
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory

class Token(BaseModel):
    access_token: str
    token_type: str

class SwaggerTokenController(BaseController):
    def __init__(self, params: OAuth2PasswordRequestForm):
        self.config = Config()
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.user_services = UserServices()

    def execute(self) -> Token | Any:
        try:
            user_res = self.user_services.get_user_by_username(self.params.username)
            if user_res is None:
                return BasePresenter.forbidden()

            is_authenticated = CryptoHelper.check_password(
                self.params.password,
                user_res.hashed_password,
                user_res.salt
            )

            if not is_authenticated:
                return BasePresenter.forbidden()

            user_presenter = UserPresenter.from_dto(user_res)

            access_token_expires = self.config.get("ACCESS_TOKEN_EXPIRE_DAYS")
            access_token_expires = timedelta(days=int(access_token_expires))
            access_token = CryptoHelper.create_access_token(
                user_presenter, access_token_expires)

            return Token(access_token=access_token, token_type="bearer")

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(UserErrMsg.FAIL_LOGIN_USER.value)
