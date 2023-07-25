from uuid import uuid4

from fastapi import HTTPException, status

from app.infra.repo.interface.music import IMusicRepo
from app.models.domain.music import Music
from app.models.scheme.music.new_music import NewMusicScheme


class NewMusicUsecase:
    def __init__(
        self,
        music_repo: IMusicRepo,
    ) -> None:
        self._music_repo = music_repo

    def execute(
        self,
        new_music: NewMusicScheme,
        user_id: int,
    ):
        if (
            not new_music.music_file.filename
            or new_music.music_file.filename.split(".")[-1] != "mp3"
        ):
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="فرمت فایل معتبر نیست.",
            )
        new_music_file_name = f"{uuid4()}.mp3"
        music = Music(
            user_id=user_id,
            title=new_music.title,
            artist=new_music.artist,
            file_name=new_music_file_name,
        )
        music_path = f"app/upload/{new_music_file_name}"
        with open(music_path, "wb") as f:
            f.write(new_music.music_file.file.read())
        self._music_repo.insert(music)
