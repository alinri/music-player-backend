from app.infra.repo.interface.music import IMusicRepo
from app.models.scheme.music.music_out import MusicOutScheme


class ListMusicUsecase:
    def __init__(
        self,
        music_repo: IMusicRepo,
    ) -> None:
        self._music_repo = music_repo

    def execute(
        self,
        user_id: int,
    ) -> list[MusicOutScheme]:
        music_list = self._music_repo.list_by_user_id(
            user_id,
        )
        music_out_list = list()
        for music in music_list:
            music_out_list.append(
                MusicOutScheme(
                    music_id=music.music_id,
                    title=music.title,
                    artist=music.artist,
                    file_name=music.file_name,
                    created_at=music.created_at,
                    modified_at=music.modified_at,
                )
            )
        return music_out_list
