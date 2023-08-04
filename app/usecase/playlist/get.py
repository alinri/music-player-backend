from fastapi import HTTPException, status

from app.infra.repo.interface.playlist import IPlayListRepo
from app.models.scheme.playlist.playlist_out import PlayListOutScheme


class GetPlayListUsecase:
    def __init__(
        self,
        palylist_repo: IPlayListRepo,
    ) -> None:
        self._palylist_repo = palylist_repo

    def execute(
        self,
        playlist_id: int,
    ) -> PlayListOutScheme:
        playlist = self._palylist_repo.get_playlist_by_id(
            playlist_id,
        )
        if not playlist:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="Playlist not found",
            )
        playlist = PlayListOutScheme(
            playlist_id=playlist.user_id,
            name=playlist.name,
            description=playlist.description,
            created_at=playlist.created_at,
            modified_at=playlist.modified_at,
        )

        return playlist
