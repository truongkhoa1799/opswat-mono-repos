from typing import Annotated

from fastapi import APIRouter, Path, Depends

from src.app.controllers.base import BaseProcess
from src.app.controllers.reaction.react_article import ReactArticleController
from src.app.dtos.reaction import ReactionParams
from src.app.dtos.user import UserResponse
from src.app.middlewares.auth import AuthMiddleware
from src.common.enums import ReactionType

router = APIRouter(
    prefix="/articles",
    responses={404: {"description": "Not found"}},
)


@router.post("/{article_id}/favorite")
async def favorite_article(
    current_user: Annotated[UserResponse | None, Depends(AuthMiddleware.get_current_user)],
    article_id: int = Path(title="The ID of the item to get")
):
    params = ReactionParams(
        reaction_type=ReactionType.Favorite.value,
        user_id=current_user.id,
        article_id=article_id
    )

    process = BaseProcess(ReactArticleController(params))
    return process.execute()


@router.delete("/{article_id}/favorite")
async def favorite_article(
    current_user: Annotated[UserResponse, Depends(AuthMiddleware.get_current_user)],
    article_id: int = Path(title="The ID of the item to get")
):
    params = ReactionParams(
        reaction_type=ReactionType.UnFavorite.value,
        user_id=current_user.id,
        article_id=article_id
    )

    process = BaseProcess(ReactArticleController(params))
    return process.execute()
