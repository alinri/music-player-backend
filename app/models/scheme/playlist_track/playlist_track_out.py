from datetime import datetime

from pydantic import BaseModel, Field


class PlayListTrackOutScheme(BaseModel):
    playlist_track_id: int
    playlist_id: int
    music_id: int
    index: int
    title: str = Field(
        max_length=255,
    )
    artist: str = Field(
        max_length=255,
    )
    file_name: str = Field(
        max_length=40,
    )
    created_at: datetime
    modified_at: datetime
