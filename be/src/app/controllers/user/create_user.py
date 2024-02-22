from src.app.controllers.base import BaseController
from src.app.dtos.user import CreateUserParams
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UserPresenter
from src.common.messages import UserErrMsg
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class CreateUserController(BaseController):
    def __init__(self, params: CreateUserParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.user_services = UserServices()

    def execute(self) -> BasePresenter[UserPresenter]:
        try:
            user_res = self.user_services.create_user(self.params)
            if user_res is not None:
                presenter = UserPresenter.from_dto(user_res)
                return BasePresenter.success(presenter)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(UserErrMsg.FAIL_CREATE_USER.value)