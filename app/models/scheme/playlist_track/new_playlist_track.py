from pydantic import BaseModel


class NewPlayListTrackScheme(BaseModel):
    playlist_id: int
    music_id: int
