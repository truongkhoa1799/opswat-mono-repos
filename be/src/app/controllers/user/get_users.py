from pydantic import BaseModel

from src.app.controllers.base import BaseController, BaseControllerWithRole
from src.app.dtos.user import GetUsersParams, UserResponse
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UsersPresenter
from src.common.messages import UserErrMsg
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class GetUsersController(BaseControllerWithRole):
    def __init__(self):
        self.logger = LoggerFactory.get_logger()
        self.user_services = UserServices()

    def is_valid(self, user: UserResponse) -> bool:
        return True

    def execute(self, params: GetUsersParams) -> BasePresenter[UsersPresenter]:
        try:
            user_responses = self.user_services.get_users(params)
            if user_responses is not None:
                presenters = UsersPresenter.from_dto(user_responses)
                return BasePresenter.success(presenters)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(UserErrMsg.FAIL_GET_USERS.value)
