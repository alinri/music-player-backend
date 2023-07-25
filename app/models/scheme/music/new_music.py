from typing import Annotated

from fastapi import File, Form, UploadFile


class NewMusicScheme:
    def __init__(
        self,
        title: Annotated[str, Form(max_length=255, min_length=1)],
        music_file: Annotated[UploadFile, File()],
        artist: Annotated[str | None, Form(max_length=255)] = None,
    ) -> None:
        self.title = title
        self.artist = artist
        self.music_file = music_file
