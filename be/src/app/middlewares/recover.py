from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from src.app.middlewares.exceptions import ValidateException, UnauthorizedException
from src.app.middlewares.exceptions import HTTPException
from src.app.presenters.base import BasePresenter


class RecoverMiddleware:
    def __init__(self, app: ASGIApp, auto_error: bool = True) -> None:
        self.app = app
        self.auto_error = auto_error

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await self.app(scope, receive, send)
        except Exception as e:
            content = BasePresenter.error(e.message)

            if isinstance(e, ValidateException):
                content = BasePresenter.bad_request(e.message)
            elif isinstance(e, HTTPException):
                content = BasePresenter.bad_request(e.message)
            elif isinstance(e, UnauthorizedException):
                content = BasePresenter.forbidden(e.message)

            response = JSONResponse(
                headers={"Content-Type": "application/json"},
                status_code=e.code,
                content=content,
            )

            await response(scope, receive, send)
            return


