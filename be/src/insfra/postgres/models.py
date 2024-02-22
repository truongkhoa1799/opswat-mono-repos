import datetime
from typing import Optional, List

from sqlmodel import Field, SQLModel

from src.common.idgen import generate_new_id
from src.common.datetime_helper import get_time, get_current


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


class ArticleModel(SQLModel, table=True):
    __tablename__ = "article"

    id: Optional[int] = Field(primary_key=True, index=True, default_factory=generate_new_id)
    title: str = Field(default='', description='title', max_length=250)
    body: str = Field(default='', description='body', max_length=10000)
    favourite_count: int = Field(default=0, description='favourite_count')
    created_at: datetime.datetime = Field(description='Birth date', default_factory=get_time)
    updated_at: datetime.datetime = Field(description='Birth date', default_factory=get_time)


