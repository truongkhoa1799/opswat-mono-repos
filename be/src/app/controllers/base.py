from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from src.app.presenters.base import BasePresenter
from src.common.messages import UserErrMsg


class BaseController(ABC):
    @abstractmethod
    def execute(self):
        pass


class BaseControllerWithRole(BaseController):

    @abstractmethod
    def is_valid(self, user: BaseModel) -> bool:
        pass


Controller = TypeVar("Controller", bound=BaseController)
Model = TypeVar("Model", bound=BaseModel | OAuth2PasswordRequestForm)


class BaseProcess(Generic[Controller, Model]):
    def __init__(self, controller: Controller, user: Model = None):
        self.controller = controller
        self.user = user

    def execute(self):
        if hasattr(self.controller, 'is_valid'):
            if self.controller.is_valid(self.user):
                return self.controller.execute()
            else:
                return BasePresenter.forbidden(UserErrMsg.DO_NOT_AUTHORIZED.value)
        else:
            return self.controller.execute()
