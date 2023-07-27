from abc import ABC, abstractmethod

from app.models.domain.user import User


class IUserRepo(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def insert_user(self, new_user: User):
        raise NotImplementedError
