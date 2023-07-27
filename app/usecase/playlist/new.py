from app.infra.repo.interface.playlist import IPlayListRepo
from app.models.domain.playlist import PlayList
from app.models.scheme.playlist.new_playlist import NewPlayListScheme


class NewPlayListUsecase:
    def __init__(
        self,
        playlist_repo: IPlayListRepo,
    ) -> None:
        self._playlist_repo = playlist_repo

    def execute(
        self,
        new_playlist: NewPlayListScheme,
        user_id: int,
    ):
        playlist = PlayList(
            user_id=user_id,
            name=new_playlist.name,
            description=new_playlist.description,
        )
        self._playlist_repo.insert(playlist)
