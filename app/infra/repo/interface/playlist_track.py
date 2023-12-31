from abc import ABC, abstractmethod

from app.models.domain.playlist_track import PlayListTrack


class IPlayListTrackRepo(ABC):
    @abstractmethod
    def insert(
        self,
        new_track: PlayListTrack,
    ):
        raise NotImplementedError

    @abstractmethod
    def list_by_playlist_id(
        self,
        playlist_id: int,
    ) -> list[PlayListTrack]:
        raise NotImplementedError

    def get_last_playlist_track(
        self,
        playlist_id: int,
    ) -> PlayListTrack | None:
        raise NotImplementedError
