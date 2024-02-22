from typing import Optional
from pydantic import Field
from src.domain.entities.base import BaseEntity


class Article(BaseEntity):
    title: str
    body: str


class ArticleEntity(Article):
    id: Optional[int] = Field(default=None)


class CreateArticleEntity(ArticleEntity):
    created_by: int


class UpdateArticleEntity(ArticleEntity):
    pass


