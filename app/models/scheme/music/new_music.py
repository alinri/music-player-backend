from typing import Annotated

from fastapi import File, Form, UploadFile


class NewMusicScheme:
    def __init__(
        self,
        title: Annotated[str, Form()],
        artist: Annotated[str | None, Form(default=None)],
        music_file: Annotated[UploadFile, File()],
    ) -> None:
        self.title = title
        self.artist = artist
        self.music_file = music_file
