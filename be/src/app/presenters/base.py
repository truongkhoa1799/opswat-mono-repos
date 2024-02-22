from typing import TypeVar, Generic
from dataclasses import dataclass, asdict
from http import HTTPStatus


T = TypeVar('T')


@dataclass
class BasePresenter(Generic[T]):
    status: int
    message: str = ''
    data: T = None

    @classmethod
    def success(cls, data: T = None):
        response = BasePresenter(HTTPStatus.OK.value, '', data)
        return asdict(response)

    @classmethod
    def error(cls, message: str = '', data: T = None):
        response = BasePresenter(HTTPStatus.INTERNAL_SERVER_ERROR.value, message, data)
        return asdict(response)

    @classmethod
    def bad_request(cls, message: str = '', data: T = None):
        response = BasePresenter(HTTPStatus.BAD_REQUEST.value, message, data)
        return asdict(response)

    @classmethod
    def forbidden(cls, message: str = '', data: T = None):
        response = BasePresenter(HTTPStatus.FORBIDDEN.value, message, data)
        return asdict(response)
