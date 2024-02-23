from typing import List

from src.app.dtos.reaction import ReactionParams
from src.app.dtos.user import UserResponse, CreateUserParams, GetUsersParams, DeleteUserParams
from src.common.crypto_helper import CryptoHelper
from src.common.enums import ReactionType
from src.common.singleton import SingletonMeta
from src.domain.entities.reaction import ReactionEntity, CreateReactionEntity, UpdateReactionEntity
from src.domain.entities.user import CreateUserEntity
from src.domain.repositories.reaction.interface import ReactionRepositoryInterface
from src.domain.repositories.reaction.mysql import ReactionPostgresRepository
from src.insfra.logger import LoggerFactory


class ReactionServices(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = LoggerFactory.get_logger()
        self.reaction_repos: ReactionRepositoryInterface = ReactionPostgresRepository()

    def react_article(self, params: ReactionParams) -> bool:
        try:
            reaction_model = self.reaction_repos.get_by_article_id_user_id(params)
            if reaction_model is None:
                create_entity = CreateReactionEntity(
                    user_id=params.user_id,
                    article_id=params.article_id,
                    reaction_type=params.reaction_type
                )
                self.reaction_repos.create(create_entity)
            elif reaction_model.type == params.reaction_type:
                return True
            elif reaction_model.type != params.reaction_type:
                update_entity = UpdateReactionEntity(
                    user_id=params.user_id,
                    article_id=params.article_id,
                    reaction_type=params.reaction_type
                )

                self.reaction_repos.update(reaction_model, update_entity.model_dump())

            return True
        except Exception as e:
            self.logger.log_error(e.__str__())
            return False

    def un_react_article(self, params: ReactionParams) -> bool:
        try:
            reaction_model = self.reaction_repos.get_by_article_id_user_id(params)
            if reaction_model is None:
                return True
            else:
                self.reaction_repos.remove_by_article_id_user_id(params)

            return True
        except Exception as e:
            self.logger.log_error(e.__str__())
            return False

    def remove_article_reactions(self, article_id: int) -> bool:
        try:
            result = self.reaction_repos.remove_by_article_id(article_id)
            return result
        except Exception as e:
            self.logger.log_error(e.__str__())
            return False
