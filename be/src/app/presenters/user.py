from dataclasses import dataclass
from typing import List

from src.app.dtos.user import UserResponse


@dataclass
class UserPresenter:
    id: int
    email: str
    username: str
    fullname: str
    created_at: str
    updated_at: str

    @staticmethod
    def from_dto(dto: UserResponse):
        presenter = UserPresenter(
            id=dto.id,
            email=dto.email,
            username=dto.username,
            fullname=dto.fullname,
            created_at=dto.created_at,
            updated_at=dto.updated_at
        )

        return presenter


@dataclass
class UsersPresenter:
    users: List[UserPresenter]
    total: int

    @staticmethod
    def from_dto(dtos: List[UserResponse]):
        users_presenter = [UserPresenter.from_dto(dto) for dto in dtos]
        presenter = UsersPresenter(
            users=users_presenter,
            total=len(dtos)
        )

        return presenter
