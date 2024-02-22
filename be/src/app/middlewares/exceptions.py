from http import HTTPStatus


class ValidateException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = HTTPStatus.BAD_REQUEST.value
        super().__init__(self.message)


class HTTPException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = HTTPStatus.BAD_REQUEST.value
        super().__init__(self.message)


class UnauthorizedException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = HTTPStatus.UNAUTHORIZED.value
        super().__init__(self.message)
