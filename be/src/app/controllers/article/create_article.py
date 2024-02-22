from pydantic import BaseModel

from src.app.controllers.base import BaseControllerWithRole
from src.app.dtos.article import CreateArticleParams
from src.app.presenters.article import ArticlePresenter
from src.app.presenters.base import BasePresenter
from src.common.messages import ArticleErrMsg
from src.domain.services.article import ArticleServices
from src.insfra.logger import LoggerFactory


class CreateArticleController(BaseControllerWithRole):
    def __init__(self, params: CreateArticleParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.article_services = ArticleServices()

    def is_valid(self, user: BaseModel) -> bool:
        return True

    def execute(self) -> BasePresenter[ArticlePresenter]:
        try:
            user_res = self.article_services.create_article(self.params)
            if user_res is not None:
                presenter = ArticlePresenter.from_dto(user_res)
                return BasePresenter.success(presenter)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(ArticleErrMsg.FAIL_CREATE_ARTICLE.value)