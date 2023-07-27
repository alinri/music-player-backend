from app.infra.repo.interface.playlist import IPlayListRepo
from app.models.scheme.playlist.playlist_out import PlayListOutScheme


class ListPlayListUsecase:
    def __init__(
        self,
        palylist_repo: IPlayListRepo,
    ) -> None:
        self._palylist_repo = palylist_repo

    def execute(
        self,
        user_id: int,
    ) -> list[PlayListOutScheme]:
        playlists = self._palylist_repo.list_by_user_id(
            user_id,
        )
        playlist_out_list = list()
        for playlist in playlists:
            playlist_out_list.append(
                PlayListOutScheme(
                    playlist_id=playlist.playlist_id,
                    name=playlist.name,
                    description=playlist.description,
                    created_at=playlist.created_at,
                    modified_at=playlist.modified_at,
                )
            )
        return playlist_out_list
