from pydantic import BaseModel

from src.app.controllers.base import BaseController, BaseControllerWithRole
from src.app.dtos.article import GetArticlesParams, ArticleResponse
from src.app.dtos.user import GetUsersParams, UserResponse
from src.app.presenters.article import ArticlesPresenter
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UsersPresenter
from src.common.messages import UserErrMsg, ArticleErrMsg
from src.domain.services.article import ArticleServices
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class GetArticlesController(BaseControllerWithRole):
    def __init__(self, params: GetArticlesParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.article_services = ArticleServices()

    def is_valid(self, user: ArticleResponse) -> bool:
        return True

    def execute(self) -> BasePresenter[ArticleResponse]:
        try:
            article_responses = self.article_services.get_articles(self.params)
            if article_responses is not None:
                presenters = ArticlesPresenter.from_dto(article_responses)
                return BasePresenter.success(presenters)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(ArticleErrMsg.FAIL_GET_ARTICLES.value)
