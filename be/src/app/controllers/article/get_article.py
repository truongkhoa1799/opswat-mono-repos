from pydantic import BaseModel

from src.app.controllers.base import BaseControllerWithRole
from src.app.dtos.article import GetArticlesParams, ArticleResponse, GetArticleParams
from src.app.presenters.article import ArticlesPresenter, ArticlePresenter
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UserPresenter
from src.common.messages import ArticleErrMsg
from src.domain.services.article import ArticleServices
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class GetArticleController(BaseControllerWithRole):
    def __init__(self, params: GetArticleParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.article_services = ArticleServices()
        self.user_services = UserServices()

    def is_valid(self, user: ArticleResponse) -> bool:
        return True

    def execute(self) -> BasePresenter[ArticlePresenter]:
        try:
            article_res = self.article_services.get_article_by_id(self.params.id)
            if article_res is None:
                return BasePresenter.error(ArticleErrMsg.FAIL_GET_ARTICLES.value)

            presenter = ArticlePresenter.from_dto(article_res)
            user_res = self.user_services.get_user(article_res.created_by)
            user_presenter = UserPresenter.from_dto(user_res)
            presenter.user = user_presenter

            return BasePresenter.success(presenter)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(ArticleErrMsg.FAIL_GET_ARTICLES.value)
