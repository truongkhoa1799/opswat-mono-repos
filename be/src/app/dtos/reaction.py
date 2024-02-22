from typing import List

from pydantic import BaseModel, Field

from src.app.dtos.base import BaseSearchParams
from src.app.dtos.user import UserResponse
from src.common.datetime_helper import get_time_str, Format
from src.common.enums import ReactionType
from src.insfra.postgres import ArticleModel, ReactionModel


class BaseReactionParams(BaseModel):
    reaction_type: str = Field(
        default=ReactionType.Favorite.value,
        title="reaction_type",
        max_length=30,
        alias='reaction_type',
    )
    user_id: int = Field(
        default=0,
        title="user_id",
        alias='user_id',
    )
    article_id: int = Field(
        default=0,
        title="article_id",
        alias='article_id',
    )


class ReactionParams(BaseReactionParams):
    pass

