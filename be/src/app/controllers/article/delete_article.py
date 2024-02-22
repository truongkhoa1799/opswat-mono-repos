from src.app.controllers.base import BaseControllerWithRole
from src.app.dtos.article import DeleteArticleParams
from src.app.dtos.user import UserResponse, DeleteUserParams
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UsersPresenter
from src.common.messages import UserErrMsg, ArticleErrMsg
from src.domain.services.article import ArticleServices
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class DeleteArticleController(BaseControllerWithRole):
    def __init__(self, params: DeleteArticleParams):
        self.logger = LoggerFactory.get_logger()
        self.params = params
        self.article_services = ArticleServices()

    def is_valid(self, user: UserResponse) -> bool:
        article_res = self.article_services.get_article_by_id(self.params.id)
        if article_res is None or article_res.created_by != user.id:
            return False

        return True

    def execute(self) -> BasePresenter[bool]:
        try:
            result = self.article_services.delete_article(self.params)
            if result:
                return BasePresenter.success(result)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(ArticleErrMsg.FAIL_DELETE_ARTICLE.value)
