from datetime import datetime, timedelta, timezone

import bcrypt
from jose import JWTError, jwt

from src.app.dtos.user import UserResponse
from src.common import Config


class CryptoHelper:

    @staticmethod
    def gen_salt() -> str:
        salt = bcrypt.gensalt()
        return bytes.decode(salt)

    @staticmethod
    def hash_password(password: str, salt: str):
        hashed_passwd = bcrypt.hashpw(str.encode(password), str.encode(salt))
        return hashed_passwd

    @staticmethod
    def check_password(password: str, hashed_password: str, salt: str):
        compared_password = CryptoHelper.hash_password(password, salt)
        compared_password = bytes.decode(compared_password)
        return compared_password == hashed_password

    @staticmethod
    def create_access_token(data: UserResponse, expires_delta: timedelta | None = None):
        config = Config()
        data = data.model_dump()
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(days=7)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            config.get("SECRET_KEY"),
            algorithm=config.get("ALGORITHM")
        )

        return encoded_jwt

    @staticmethod
    def decode_token(token: str) -> UserResponse | None:
        config = Config()
        try:
            payload = jwt.decode(token, config.get("SECRET_KEY"), algorithms=[config.get("ALGORITHM")])
            if payload is None:
                return None

            return UserResponse(**payload)

        except JWTError:
            return None


