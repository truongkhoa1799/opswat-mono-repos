from abc import ABC, abstractmethod
from typing import List

from src.app.dtos.article import GetArticlesParams
from src.domain.entities.article import CreateArticleEntity
from src.insfra.postgres import BasePostgresInterface, ArticleModel


class ArticleRepositoryInterface(BasePostgresInterface[ArticleModel, CreateArticleEntity], ABC):
    @abstractmethod
    def get_articles(self, params: GetArticlesParams) -> List[ArticleModel] | None:
        pass

    @abstractmethod
    def count_total_articles(self) -> int | None:
        pass
