from datetime import datetime

from pydantic import BaseModel


class MusicOutScheme(BaseModel):
    music_id: int
    title: str
    artist: str | None
    file_name: str
    created_at: datetime
    modified_at: datetime
