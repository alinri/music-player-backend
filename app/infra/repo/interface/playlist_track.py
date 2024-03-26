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

    @abstractmethod
    def get_last_playlist_track(
        self,
        playlist_id: int,
    ) -> PlayListTrack | None:
        raise NotImplementedError

    @abstractmethod
    def delete_playlist_track(
        self,
        track_id: int,
    ):
        raise NotImplementedError

    @abstractmethod
    def get_track_by_id(
        self,
        track_id: int,
    ) -> PlayListTrack:
        raise NotImplementedError
