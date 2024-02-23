from abc import ABC, abstractmethod
from typing import List

from src.app.dtos.reaction import ReactionParams
from src.domain.entities.reaction import CreateReactionEntity
from src.insfra.postgres import BasePostgresInterface, ReactionModel


class ReactionRepositoryInterface(BasePostgresInterface[ReactionModel, CreateReactionEntity], ABC):
    @abstractmethod
    def count_reactions_by_article_id(self, article_id: int) -> List[ReactionModel] | None:
        pass

    @abstractmethod
    def get_by_article_id_user_id(self, params: ReactionParams) -> ReactionModel | None:
        pass

    @abstractmethod
    def remove_by_article_id_user_id(self, params: ReactionParams) -> ReactionModel | None:
        pass

    @abstractmethod
    def remove_by_article_id(self, article_id: int) -> bool | None:
        pass
