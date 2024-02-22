import functools
from http import HTTPStatus, HTTPMethod
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt, JWTError
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from starlette.datastructures import Headers

from src.app.dtos.user import UserResponse
from src.app.middlewares.exceptions import HTTPException, UnauthorizedException
from src.app.presenters.base import BasePresenter
from src.common import Config
from src.common.crypto_helper import CryptoHelper
from src.common.messages import UserErrMsg

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

WHITELIST_URLS = [
    {"method": "POST", "path": "/api/auth/login"}
]


class AuthMiddleware:
    def __init__(self, app: ASGIApp, auto_error: bool = True) -> None:
        self.app = app
        self.auto_error = auto_error

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        headers = Headers(scope=scope)
        path = scope.get("path")
        method = scope.get("method")
        if AuthMiddleware.is_allow_forward(path, method):
            await self.app(scope, receive, send)
            return

        response = self.get_token(headers)
        if isinstance(response, JSONResponse):
            await response(scope, receive, send)
            return

        user_response = CryptoHelper.decode_token(response)
        if user_response is None:
            response = AuthMiddleware.create_unauthorized_response()
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)

    @staticmethod
    def get_token(headers: Headers) -> str | JSONResponse:
        authorization = headers.get("Authorization")
        scheme, token = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            return AuthMiddleware.create_unauthorized_response()

        return token

    @staticmethod
    def create_unauthorized_response() -> JSONResponse:
        res = BasePresenter.bad_request(UserErrMsg.DO_NOT_AUTHORIZED.value)
        return JSONResponse(
            headers={"Content-Type": "application/json"},
            status_code=HTTPStatus.BAD_REQUEST.value,
            content=res,
        )

    @staticmethod
    def is_allow_forward(path, method) -> bool:
        def check(acc, item):
            return acc or (item["method"] == method and item["path"] == path)

        # Use reduce to check if the condition is True for any item in the list
        return functools.reduce(check, WHITELIST_URLS, False)

    @staticmethod
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserResponse:
        try:
            user_response = CryptoHelper.decode_token(token)
            if user_response is None:
                raise UnauthorizedException(message="Could not validate credentials")

            return user_response

        except JWTError:
            raise UnauthorizedException(message="Could not validate credentials")



