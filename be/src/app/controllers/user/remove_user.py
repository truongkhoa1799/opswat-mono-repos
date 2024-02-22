from src.app.controllers.base import BaseControllerWithRole
from src.app.dtos.user import UserResponse, DeleteUserParams
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UsersPresenter
from src.common.messages import UserErrMsg
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class DeleteUserController(BaseControllerWithRole):
    def __init__(self, params: DeleteUserParams):
        self.logger = LoggerFactory.get_logger()
        self.params = params
        self.user_services = UserServices()

    def is_valid(self, user: UserResponse) -> bool:
        if user.email == self.params.email:
            return False

        return True

    def execute(self) -> BasePresenter[bool]:
        try:
            user_responses = self.user_services.delete_user(self.params)
            if user_responses:
                return BasePresenter.success(user_responses)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(UserErrMsg.FAIL_DELETE_USERS.value)