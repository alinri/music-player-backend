from fastapi import HTTPException, status

from app.infra.repo.interface.playlist import IPlayListRepo
from app.infra.repo.interface.playlist_track import IPlayListTrackRepo
from app.models.scheme.playlist_track.playlist_track_out import (
    PlayListTrackOutScheme,
)


class ListPlayListTrackUsecase:
    def __init__(
        self,
        playlist_track_repo: IPlayListTrackRepo,
        playlist_repo: IPlayListRepo,
    ) -> None:
        self._playlist_track_repo = playlist_track_repo
        self._playlist_repo = playlist_repo

    def execute(
        self,
        playlist_id: int,
    ) -> list[PlayListTrackOutScheme]:
        playlist_exist = self._playlist_repo.get_playlist_by_id(
            playlist_id,
        )
        if not playlist_exist:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="لیست پخش موجود نیست.",
            )

        playlist_tracks = self._playlist_track_repo.list_by_playlist_id(
            playlist_id,
        )

        out_tracks = list()

        for track in playlist_tracks:
            out_tracks.append(
                PlayListTrackOutScheme(
                    playlist_track_id=track.playlist_track_id,
                    playlist_id=track.playlist_id,
                    music_id=track.music_id,
                    index=track.index,
                    title=track.music.title,
                    artist=track.music.artist,
                    file_name=track.music.file_name,
                    created_at=track.created_at,
                    modified_at=track.modified_at,
                )
            )
        return out_tracks
