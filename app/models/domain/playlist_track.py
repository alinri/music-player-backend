from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.db.base import Base

if TYPE_CHECKING:
    from .music import Music


class PlayListTrack(Base):
    __tablename__ = "playlist_track"

    playlist_track_id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    playlist_id: Mapped[int] = mapped_column(
        ForeignKey("playlist.playlist_id"),
    )

    music_id: Mapped[int] = mapped_column(
        ForeignKey("music.music_id"),
    )

    music: Mapped["Music"] = relationship()

    index: Mapped[int]

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
    )
    modified_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    )
