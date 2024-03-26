from app.infra.repo.interface.playlist_track import IPlayListTrackRepo
from app.models.scheme.playlist_track.playlist_track_out import (
    PlayListTrackOutScheme,
)


class DeletePlayListTrackUsecase:
    def __init__(
        self,
        playlist_track_repo: IPlayListTrackRepo,
    ) -> None:
        self._playlist_track_repo = playlist_track_repo

    def execute(
        self,
        track_id: int,
    ) -> list[PlayListTrackOutScheme]:
        self._playlist_track_repo.delete_playlist_track(track_id)
