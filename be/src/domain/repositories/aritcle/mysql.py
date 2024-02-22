from typing import List

from sqlmodel import Session, select

from src.app.dtos.article import GetArticlesParams
from src.insfra.logger import LoggerFactory
from src.insfra.postgres import BasePostgres, ArticleModel

from .interface import ArticleRepositoryInterface
from ...entities.article import CreateArticleEntity


class ArticlePostgresRepository(BasePostgres[ArticleModel, CreateArticleEntity], ArticleRepositoryInterface):
    def __init__(self):
        self.logger = LoggerFactory.get_logger()
        super().__init__(ArticleModel)

    def get_articles(self, params: GetArticlesParams) -> List[ArticleModel] | None:
        try:
            with Session(self.engine) as session:
                query = select(self.model).offset(params.offset).limit(params.limit)
                result = session.exec(query).all()
                articles = [article for article in result]
                return articles

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None
