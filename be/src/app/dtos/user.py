from pydantic import BaseModel, Field, field_validator

from src.app.dtos.base import BaseSearchParams
from src.app.middlewares.exceptions import ValidateException
from src.common.datetime_helper import get_time_str, Format
from src.insfra.postgres import UserModel


# -------------- Params --------------
class BaseUserParams(BaseModel):
    email: str = Field(
        default=None,
        title="User email",
        alias='email',
        max_length=255,
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    username: str = Field(
        default=None,
        title="Username",
        min_length=5,
        max_length=20,
        alias='username',
    )
    fullname: str = Field(
        default=None,
        title="User fullname",
        min_length=3,
        max_length=40,
        alias='fullname',
    )


class CreateUserParams(BaseUserParams):
    password: str = Field(
        default=None,
        title="User ID",
        min_length=8,
        max_length=30,
        alias='password',
    )

    @field_validator('password', mode='before')
    def password_complexity(cls, v):
        # Additional custom validation for password complexity
        if not any(c.isupper() for c in v):
            raise ValidateException('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValidateException('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValidateException('Password must contain at least one digit')
        return v


class GetUsersParams(BaseSearchParams):
    pass


class DeleteUserParams(BaseModel):
    email: str = Field(
        default=None,
        title="User email",
        alias='email',
        max_length=255,
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )


# -------------- Response --------------
class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    fullname: str
    hashed_password: str
    salt: str
    created_at: str
    updated_at: str

    @staticmethod
    def from_model(model: UserModel):
        return UserResponse(
            id=model.id,
            email=model.email,
            username=model.username,
            fullname=model.fullname,
            hashed_password=model.hashed_password,
            salt=model.salt,
            created_at=get_time_str(model.created_at, Format.DATE),
            updated_at=get_time_str(model.updated_at, Format.DATE),
        )
