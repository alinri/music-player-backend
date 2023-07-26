from abc import ABC, abstractmethod

from app.models.domain.playlist import PlayList


class IPlayListRepo(ABC):
    @abstractmethod
    def insert(self, new_playlist: PlayList):
        raise NotImplementedError

    @abstractmethod
    def list_by_user_id(self, user_id: int) -> list[PlayList]:
        raise NotImplementedError
