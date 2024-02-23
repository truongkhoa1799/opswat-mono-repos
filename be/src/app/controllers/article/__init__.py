from typing import Annotated

from fastapi import APIRouter, Query, Depends, Path, Form

from src.app.controllers.article.get_article import GetArticleController
from src.app.presenters.user import UserPresenter

from src.app.controllers.article.create_article import CreateArticleController
from src.app.controllers.article.delete_article import DeleteArticleController
from src.app.controllers.article.get_articles import GetArticlesController
from src.app.controllers.article.update_article import UpdateArticleController
from src.app.controllers.base import BaseProcess
from src.app.dtos.article import CreateArticleParams, UpdateArticleParams, GetArticlesParams, DeleteArticleParams, \
    GetArticleParams
from src.app.middlewares.auth import AuthMiddleware

router = APIRouter(
    prefix="/articles",
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_articles(
    limit: int = Query(10, description="limit", ge=0, lt=100),
    offset: int = Query(0, description="offset", ge=0, lt=100),
):
    params = GetArticlesParams(limit=limit, offset=offset)
    process = BaseProcess(GetArticlesController(params))
    return process.execute()


@router.get("/{article_id}")
async def get_article(
    article_id: int = Path(title="The ID of the item to get")
):
    params = GetArticleParams(id=article_id)
    process = BaseProcess(GetArticleController(params))
    return process.execute()


@router.post("/")
async def create_article(
    current_user: Annotated[UserPresenter | None, Depends(AuthMiddleware.get_current_user)],
    title: Annotated[str, Form()],
    body: Annotated[str, Form()],
):
    params = CreateArticleParams(
        title=title, body=body, created_by=current_user.id)
    process = BaseProcess(CreateArticleController(params))
    return process.execute()


@router.put("/{article_id}")
async def update_article(
    current_user: Annotated[UserPresenter | None, Depends(AuthMiddleware.get_current_user)],
    title: Annotated[str, Form()],
    body: Annotated[str, Form()],
    article_id: int = Path(title="The ID of the item to get")
):
    params = UpdateArticleParams(title=title, body=body, id=article_id)
    process = BaseProcess(UpdateArticleController(params), current_user)
    return process.execute()


@router.delete("/{article_id}")
async def delete_article(
    current_user: Annotated[UserPresenter | None, Depends(AuthMiddleware.get_current_user)],
    article_id: int = Path(title="The ID of the item to get")
):
    params = DeleteArticleParams(id=article_id)
    process = BaseProcess(DeleteArticleController(params), current_user)
    return process.execute()
