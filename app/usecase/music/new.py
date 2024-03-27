import shutil
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
        accepted_formats = ["mp3", "m4a", "aac"]
        if (
            not new_music.music_file.filename
            or (file_format := new_music.music_file.filename.split(".")[-1])
            not in accepted_formats
        ):
            raise HTTPException(
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="فرمت فایل معتبر نیست.",
            )
        new_music_file_name = f"{uuid4()}.{file_format}"
        music = Music(
            user_id=user_id,
            title=new_music.title,
            artist=new_music.artist,
            file_name=new_music_file_name,
        )
        music_path = f"app/upload/{new_music_file_name}"
        try:
            with open(music_path, "wb") as f:
                shutil.copyfileobj(new_music.music_file.file, f)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in uploading file",
            )
        finally:
            new_music.music_file.file.close()
        self._music_repo.insert(music)
