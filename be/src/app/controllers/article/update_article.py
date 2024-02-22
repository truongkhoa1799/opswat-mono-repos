from pydantic import BaseModel

from src.app.controllers.base import BaseControllerWithRole
from src.app.dtos.article import UpdateArticleParams
from src.app.presenters.article import ArticlePresenter
from src.app.presenters.base import BasePresenter
from src.common.messages import ArticleErrMsg
from src.domain.services.article import ArticleServices
from src.insfra.logger import LoggerFactory


class UpdateArticleController(BaseControllerWithRole):
    def __init__(self, params: UpdateArticleParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.article_services = ArticleServices()

    def is_valid(self, user: BaseModel) -> bool:
        # TODO: Check owners of article
        return True

    def execute(self) -> BasePresenter[ArticlePresenter]:
        try:
            article_model = self.article_services.update_article(self.params)
            if article_model is not None:
                presenter = ArticlePresenter.from_dto(article_model)
                return BasePresenter.success(presenter)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(ArticleErrMsg.FAIL_UPDATE_ARTICLE.value)