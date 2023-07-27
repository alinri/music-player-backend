from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.db.base import Base

if TYPE_CHECKING:
    from .playlist_track import PlayListTrack
    from .user import User


class PlayList(Base):
    __tablename__ = "playlist"

    playlist_id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.user_id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="playlists",
    )
    playlist_tracks: Mapped[list["PlayListTrack"]] = relationship()
    name: Mapped[str] = mapped_column(
        String(255),
    )
    description: Mapped[Optional[str]] = mapped_column(
        String(1024),
    )
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
    )
    modified_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    )
