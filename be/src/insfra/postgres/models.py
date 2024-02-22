import datetime
from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from src.common.enums import ReactionType
from src.common.idgen import generate_new_id
from src.common.datetime_helper import get_time, get_current


class ReactionModel(SQLModel, table=True):
    __tablename__ = "reaction"

    user_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="user.id", index=True)
    article_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="article.id", index=True)
    type: str = Field(default=ReactionType.Favorite.value, description='type', max_length=30)

    created_at: datetime.datetime = Field(description='Created At', default_factory=get_current)
    updated_at: datetime.datetime = Field(description='Updated At', default_factory=get_current)


class UserModel(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(primary_key=True, index=True, default_factory=generate_new_id)
    email: str = Field(default='', description='Email', max_length=255, unique=True)
    username: str = Field(default='', description='Username', max_length=255, unique=True)
    fullname: str = Field(default='', description='Full name', max_length=255)
    salt: str = Field(default='', description='salt', max_length=255)
    hashed_password: str = Field(description='hashed_password', max_length=255, default_factory=get_current)
    created_at: datetime.datetime = Field(description='Created At', default_factory=get_current)
    updated_at: datetime.datetime = Field(description='Updated At', default_factory=get_current)

    reacted_articles: List["ArticleModel"] = Relationship(back_populates="reacted_users", link_model=ReactionModel)
    # articles: List["ArticleModel"] = Relationship(back_populates="created_user")


class ArticleModel(SQLModel, table=True):
    __tablename__ = "article"

    id: Optional[int] = Field(primary_key=True, index=True, default_factory=generate_new_id)
    title: str = Field(default='', description='title', max_length=250)
    body: str = Field(default='', description='body', max_length=10000)
    created_at: datetime.datetime = Field(description='Created At', default_factory=get_current)
    updated_at: datetime.datetime = Field(description='Updated At', default_factory=get_current)

    created_by: Optional[int] = Field(default=None, description='created_by', foreign_key="user.id", index=True)
    # created_user: Optional[UserModel] = Relationship(back_populates="articles")

    reacted_users: List["UserModel"] = Relationship(back_populates="reacted_articles", link_model=ReactionModel)




