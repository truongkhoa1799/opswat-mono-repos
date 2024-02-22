from src.app.controllers.base import BaseController
from src.app.dtos.reaction import ReactionParams
from src.app.presenters.base import BasePresenter
from src.common.enums import ReactionType
from src.common.messages import ArticleErrMsg
from src.domain.services.article import ArticleServices
from src.domain.services.reaction import ReactionServices
from src.insfra.logger import LoggerFactory


class ReactArticleController(BaseController):
    def __init__(self, params: ReactionParams):
        self.params = params
        self.logger = LoggerFactory.get_logger()
        self.reaction_services = ReactionServices()
        self.article_services = ArticleServices()

    def execute(self) -> BasePresenter[bool]:
        try:
            article_res = self.article_services.get_article_by_id(self.params.article_id)
            if article_res is None:
                return BasePresenter.error(ArticleErrMsg.ARTICLE_NOT_EXIST.value)

            if self.params.reaction_type == ReactionType.Favorite.value:
                user_res = self.reaction_services.react_article(self.params)
                return BasePresenter.success(user_res)

            elif self.params.reaction_type == ReactionType.UnFavorite.value:
                user_res = self.reaction_services.un_react_article(self.params)
                return BasePresenter.success(user_res)

        except Exception as e:
            self.logger.log_error(e.__str__())

        return BasePresenter.error(ArticleErrMsg.FAIL_REACT_ARTICLE.value)