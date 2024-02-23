from typing import List

from src.app.dtos.article import CreateArticleParams, ArticleResponse, GetArticlesParams, DeleteArticleParams, \
    UpdateArticleParams
from src.common.singleton import SingletonMeta
from src.domain.entities.article import CreateArticleEntity, UpdateArticleEntity
from src.domain.repositories.aritcle.interface import ArticleRepositoryInterface
from src.domain.repositories.aritcle.mysql import ArticlePostgresRepository
from src.domain.repositories.reaction.interface import ReactionRepositoryInterface
from src.domain.repositories.reaction.mysql import ReactionPostgresRepository
from src.insfra.logger import LoggerFactory


class ArticleServices(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = LoggerFactory.get_logger()
        self.article_repos: ArticleRepositoryInterface = ArticlePostgresRepository()
        self.reaction_repos: ReactionRepositoryInterface = ReactionPostgresRepository()

    def create_article(self, params: CreateArticleParams) -> ArticleResponse | None:
        try:
            entity = CreateArticleEntity(
                title=params.title,
                body=params.body,
                created_by=params.created_by
            )
            model = self.article_repos.create(entity)
            data = ArticleResponse.from_model(model, [])
            return data
        except Exception as e:
            self.logger.log_error(e.__str__())
            return None

    def get_article_by_id(self, article_id: int) -> ArticleResponse | None:
        try:
            article_model = self.article_repos.get(article_id)
            if article_model is None:
                return None

            return ArticleResponse.from_model(article_model, [])
        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def get_articles(self, params: GetArticlesParams) -> List[ArticleResponse] | None:
        try:
            article_models = self.article_repos.get_articles(params)
            if article_models is None:
                return None

            article_responses: List[ArticleResponse] = []
            for article_model in article_models:
                reactions = self.reaction_repos.count_reactions_by_article_id(
                    article_model.id)
                article_res = ArticleResponse.from_model(
                    article_model, reactions)
                article_responses.append(article_res)

            return article_responses
        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def delete_article(self, params: DeleteArticleParams) -> bool:
        try:
            user_model = self.article_repos.get(params.id)
            if user_model is None:
                return False

            self.article_repos.remove(user_model.id)
            return True
        except Exception as e:
            self.logger.log_error(e.__str__())

        return False

    def update_article(self, params: UpdateArticleParams) -> ArticleResponse | None:
        try:
            article_model = self.article_repos.get(params.id)
            if article_model is None:
                return None

            update_entity = UpdateArticleEntity(
                id=article_model.id,
                title=params.title,
                body=params.body
            )

            new_model = self.article_repos.update(
                article_model, update_entity.model_dump())
            article_response = ArticleResponse.from_model(new_model)
            return article_response

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def count_total_articles(self) -> int | None:
        try:
            total_articles = self.article_repos.count_total_articles()
            return total_articles
        except Exception as e:
            self.logger.log_error(e.__str__())

        return None
