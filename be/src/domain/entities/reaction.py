from typing import Optional
from pydantic import Field

from src.common.enums import ReactionType
from src.domain.entities.base import BaseEntity


class Reaction(BaseEntity):
    user_id: int
    article_id: int
    reaction_type: str


class ReactionEntity(Reaction):
    id: Optional[int] = Field(default=None)


class CreateReactionEntity(ReactionEntity):
    pass


class UpdateReactionEntity(ReactionEntity):
    pass


