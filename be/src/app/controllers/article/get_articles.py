from pydantic import BaseModel

from src.app.controllers.base import BaseControllerWithRole
from src.app.dtos.article import GetArticlesParams, ArticleResponse
from src.app.presenters.article import ArticlesPresenter
from src.app.presenters.base import BasePresenter
from src.app.presenters.user import UserPresenter
from src.common.messages import ArticleErrMsg
from src.domain.services.article import ArticleServices
from src.domain.services.user import UserServices
from src.insfra.logger import LoggerFactory


class GetArticlesController(BaseControllerWithRole):
    def __init__(self, params: GetArticlesParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.article_services = ArticleServices()
        self.user_services = UserServices()

    def is_valid(self, user: ArticleResponse) -> bool:
        return True

    def execute(self) -> BasePresenter[ArticlesPresenter]:
        try:
            total_articles = self.article_services.count_total_articles()
            if total_articles is None:
                return BasePresenter.error(ArticleErrMsg.FAIL_GET_ARTICLES.value)

            article_responses = self.article_services.get_articles(self.params)
            if article_responses is None:
                return BasePresenter.error(ArticleErrMsg.FAIL_GET_ARTICLES.value)

            presenters = ArticlesPresenter.from_dto(article_responses)
            for article in presenters.articles:
                user_res = self.user_services.get_user(article.user_id)
                user_presenter = UserPresenter.from_dto(user_res)
                article.user = user_presenter

            presenters.total = total_articles
            return BasePresenter.success(presenters)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(ArticleErrMsg.FAIL_GET_ARTICLES.value)
