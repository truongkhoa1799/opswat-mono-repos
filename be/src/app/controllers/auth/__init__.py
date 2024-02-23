from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.app.controllers.auth.swagger_token import SwaggerTokenController
from src.app.presenters.base import BasePresenter
from src.app.presenters.auth import AuthPresenter

from src.app.controllers.auth.login import LoginController
from src.app.controllers.base import BaseProcess

router = APIRouter(
    prefix="/auth",
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
async def login(params: Annotated[OAuth2PasswordRequestForm, Depends()]):
    process = BaseProcess(LoginController(params))
    return process.execute()


@router.post("/token")
async def token(params: Annotated[OAuth2PasswordRequestForm, Depends()]):
    process = BaseProcess(SwaggerTokenController(params))
    return process.execute()
