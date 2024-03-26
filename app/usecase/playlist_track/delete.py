from fastapi import HTTPException, status

from app.infra.repo.interface.playlist import IPlayListRepo
from app.infra.repo.interface.playlist_track import IPlayListTrackRepo


class DeletePlayListTrackUsecase:
    def __init__(
        self,
        playlist_track_repo: IPlayListTrackRepo,
        playlist_repo: IPlayListRepo,
    ) -> None:
        self._playlist_track_repo = playlist_track_repo
        self._playlist_repo = playlist_repo

    def execute(
        self,
        track_id: int,
        user_id: int,
    ):
        track_exist = self._playlist_track_repo.get_track_by_id(track_id)
        if not track_exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="track not exist!",
            )
        play_list = self._playlist_repo.get_playlist_by_id(
            track_exist.playlist_id
        )
        if play_list.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="track not exist!",
            )
        self._playlist_track_repo.delete_playlist_track(track_id)
