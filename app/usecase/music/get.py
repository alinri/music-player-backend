from fastapi import HTTPException, status

from app.infra.repo.interface.music import IMusicRepo
from app.models.scheme.music.music_out import MusicOutScheme


class GetMusicUsecase:
    def __init__(
        self,
        music_repo: IMusicRepo,
    ) -> None:
        self._music_repo = music_repo

    def execute(
        self,
        music_id: int,
    ) -> MusicOutScheme:
        music = self._music_repo.get_by_music_id(
            music_id,
        )
        if not music:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="No music found with provided id",
            )
        music_out = MusicOutScheme(
            music_id=music.music_id,
            title=music.title,
            artist=music.artist,
            file_name=music.file_name,
            created_at=music.created_at,
            modified_at=music.modified_at,
        )

        return music_out
