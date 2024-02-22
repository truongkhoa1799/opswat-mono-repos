from dataclasses import dataclass

from src.app.dtos.user import UserResponse
from src.app.presenters.user import UserPresenter


@dataclass
class AuthPresenter(UserPresenter):
    access_token: str

    @staticmethod
    def from_user_response(dto: UserResponse, access_token: str):
        presenter = AuthPresenter(
            id=dto.id,
            email=dto.email,
            username=dto.username,
            fullname=dto.fullname,
            created_at=dto.created_at,
            updated_at=dto.updated_at,
            access_token=access_token
        )

        return presenter
