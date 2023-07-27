from datetime import datetime

from pydantic import BaseModel


class PlayListOutScheme(BaseModel):
    playlist_id: int
    name: str
    description: str | None
    created_at: datetime
    modified_at: datetime
