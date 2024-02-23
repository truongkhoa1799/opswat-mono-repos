from typing import Annotated

from fastapi import APIRouter, Form, Query, Depends, HTTPException, Header, Path
from src.app.presenters.user import UserPresenter

from src.app.controllers.base import BaseProcess
from src.app.controllers.user.create_user import CreateUserController
from src.app.controllers.user.get_users import GetUsersController
from src.app.controllers.user.delete_user import DeleteUserController
from src.app.dtos.user import CreateUserParams, GetUsersParams, DeleteUserParams
from src.app.middlewares.auth import AuthMiddleware

router = APIRouter(
    prefix="/users",
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_user(
    email: Annotated[str, Form()],
    username: Annotated[str, Form()],
    fullname: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    params = CreateUserParams(
        email=email,
        username=username,
        fullname=fullname,
        password=password,
    )
    process = BaseProcess(CreateUserController(params))
    return process.execute()


@router.get("/")
async def get_users(
    limit: int = Query(10, description="limit", ge=0, lt=100),
    offset: int = Query(0, description="offset", ge=0, lt=100),
):
    params = GetUsersParams(limit=limit, offset=offset)
    process = BaseProcess(GetUsersController(params))
    return process.execute()


@router.delete("/{email}")
async def remove_users(
    current_user: Annotated[UserPresenter | None, Depends(AuthMiddleware.get_current_user)],
    email: str = Path(description="email", max_length=255,
                      regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
):
    params = DeleteUserParams(email=email)
    process = BaseProcess(DeleteUserController(params), current_user)
    return process.execute()
