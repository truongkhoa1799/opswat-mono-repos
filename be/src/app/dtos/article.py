from pydantic import BaseModel, Field

from src.app.dtos.base import BaseSearchParams
from src.common.datetime_helper import get_time_str, Format
from src.insfra.postgres import ArticleModel


class BaseArticleParams(BaseModel):
    title: str = Field(
        default='',
        title="title",
        min_length=5,
        max_length=250,
        alias='title',
    )
    body: str = Field(
        default='',
        title="body",
        min_length=3,
        max_length=10000,
        alias='body',
    )


class CreateArticleParams(BaseArticleParams):
    pass


class UpdateArticleParams(BaseArticleParams):
    id: int = Field(
        default=0,
        title="id",
        alias='id',
    )


class GetArticlesParams(BaseSearchParams):
    pass


class DeleteArticleParams(BaseSearchParams):
    id: int = Field(
        default=0,
        title="id",
        alias='id',
    )


class ArticleResponse(BaseModel):
    id: int
    title: str
    body: str
    favourite_count: int
    created_at: str
    updated_at: str

    @staticmethod
    def from_model(model: ArticleModel):
        return ArticleResponse(
            id=model.id,
            title=model.title,
            body=model.body,
            favourite_count=model.favourite_count,
            created_at=get_time_str(model.created_at, Format.DATE_TIME),
            updated_at=get_time_str(model.updated_at, Format.DATE_TIME),
        )
