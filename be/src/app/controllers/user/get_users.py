from pydantic import BaseModel

from src.app.controllers.base import BaseController, BaseControllerWithRole
from src.app.dtos.user import GetUsersParams, UserResponse
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UsersPresenter
from src.common.messages import UserErrMsg
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class GetUsersController(BaseControllerWithRole):
    def __init__(self, params: GetUsersParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.user_services = UserServices()

    def is_valid(self, user: UserResponse) -> bool:
        return True

    def execute(self) -> BasePresenter[UsersPresenter]:
        try:
            user_responses = self.user_services.get_users(self.params)
            if user_responses is not None:
                presenters = UsersPresenter.from_dto(user_responses)
                return BasePresenter.success(presenters)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(UserErrMsg.FAIL_GET_USERS.value)
