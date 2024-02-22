from dataclasses import dataclass
from typing import List

from src.app.dtos.article import ArticleResponse


@dataclass
class ArticlePresenter:
    id: int
    title: str
    body: str
    favourite_count: int
    created_at: str
    updated_at: str

    @staticmethod
    def from_dto(dto: ArticleResponse):
        presenter = ArticlePresenter(
            id=dto.id,
            title=dto.title,
            body=dto.body,
            favourite_count=dto.favourite_count,
            created_at=dto.created_at,
            updated_at=dto.updated_at
        )

        return presenter


@dataclass
class ArticlesPresenter:
    articles: List[ArticlePresenter]
    total: int

    @staticmethod
    def from_dto(dtos: List[ArticleResponse]):
        articles_presenter = [ArticlePresenter.from_dto(dto) for dto in dtos]
        presenter = ArticlesPresenter(
            articles=articles_presenter,
            total=len(dtos)
        )

        return presenter
