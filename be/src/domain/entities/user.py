from typing import Optional
from pydantic import Field
from src.domain.entities.base import BaseEntity


class User(BaseEntity):
    email: str
    username: str
    hashed_password: str
    fullname: str


class UserEntity(User):
    id: Optional[int] = Field(default=None)


class CreateUserEntity(UserEntity):
    salt: str
    pass
