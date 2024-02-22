from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.app.controllers.auth.login import LoginController
from src.app.controllers.base import BaseProcess

router = APIRouter(
    prefix="/auth",
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
async def login(params: Annotated[OAuth2PasswordRequestForm, Depends()]):
    process = BaseProcess(LoginController())
    return process.execute(params)



