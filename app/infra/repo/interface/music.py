from abc import ABC, abstractmethod

from app.models.domain.music import Music


class IMusicRepo(ABC):
    @abstractmethod
    def get_by_music_id(self, music_id: int) -> Music | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> list[Music] | None:
        raise NotImplementedError

    @abstractmethod
    def insert(self, new_user: Music):
        raise NotImplementedError

    @abstractmethod
    def list_by_user_id(self, user_id: int) -> list[Music]:
        raise NotImplementedError
