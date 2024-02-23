from typing import List

from sqlalchemy import func
from sqlmodel import Session, select, and_

from src.app.dtos.reaction import ReactionParams
from src.insfra.logger import LoggerFactory
from src.insfra.postgres import BasePostgres, ReactionModel

from .interface import ReactionRepositoryInterface
from ...entities.reaction import CreateReactionEntity


class ReactionPostgresRepository(BasePostgres[ReactionModel, CreateReactionEntity], ReactionRepositoryInterface):
    def __init__(self):
        self.logger = LoggerFactory.get_logger()
        super().__init__(ReactionModel)

    def count_reactions_by_article_id(self, article_id: int) -> List[ReactionModel] | None:
        try:
            with Session(self.engine) as session:
                statement = select(self.model).where(article_id == self.model.article_id)
                result = [i for i in session.exec(statement).all()]
                return result

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def get_by_article_id_user_id(self, params: ReactionParams) -> ReactionModel | None:
        try:
            with Session(self.engine) as session:
                statement = select(self.model).where(and_(
                    params.article_id == self.model.article_id,
                    params.user_id == self.model.user_id
                ))
                result = session.exec(statement).first()
                return result

        except Exception as e:
            self.logger.log_error(e.__str__())

        return None

    def remove_by_article_id_user_id(self, params: ReactionParams) -> bool:
        try:
            with Session(self.engine) as session:
                statement = select(self.model).where(and_(
                    params.article_id == self.model.article_id,
                    params.user_id == self.model.user_id
                ))

                model = session.exec(statement).first()
                session.delete(model)
                session.commit()

            return True

        except Exception as e:
            self.logger.log_error(e.__str__())

        return False

    def remove_by_article_id(self, article_id: int) -> bool | None:
        try:
            with Session(self.engine) as session:
                statement = select(self.model).where(article_id == self.model.article_id)
                model = session.exec(statement).first()
                session.delete(model)
                session.commit()

            return True

        except Exception as e:
            self.logger.log_error(e.__str__())

        return False
