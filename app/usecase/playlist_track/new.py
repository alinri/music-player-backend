from fastapi import HTTPException, status

from app.infra.repo.interface.music import IMusicRepo
from app.infra.repo.interface.playlist import IPlayListRepo
from app.infra.repo.interface.playlist_track import IPlayListTrackRepo
from app.models.domain.playlist_track import PlayListTrack
from app.models.scheme.playlist_track.new_playlist_track import (
    NewPlayListTrackScheme,
)


class NewPlayListTrackUsecase:
    def __init__(
        self,
        playlist_track_repo: IPlayListTrackRepo,
        playlist_repo: IPlayListRepo,
        music_repo: IMusicRepo,
    ) -> None:
        self._playlist_track_repo = playlist_track_repo
        self._playlist_repo = playlist_repo
        self._music_repo = music_repo

    def execute(
        self,
        new_track: NewPlayListTrackScheme,
    ):
        playlist_exist = self._playlist_repo.get_playlist_by_id(
            new_track.playlist_id,
        )
        if not playlist_exist:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="لیست پخش موجود نیست.",
            )
        music_exist = self._playlist_repo.get_playlist_by_id(
            new_track.music_id,
        )
        if not music_exist:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="موزیک موجود نیست.",
            )

        last_track = self._playlist_track_repo.get_last_playlist_track(
            new_track.playlist_id,
        )
        new_track_index = 0
        if last_track:
            new_track_index = last_track.index + 1

        track = PlayListTrack(
            playlist_id=new_track.playlist_id,
            music_id=new_track.music_id,
            index=new_track_index,
        )

        self._playlist_track_repo.insert(track)
