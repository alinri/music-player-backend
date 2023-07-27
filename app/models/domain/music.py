from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.db.base import Base

if TYPE_CHECKING:
    from .user import User


class Music(Base):
    __tablename__ = "music"

    music_id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.user_id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="musics",
    )
    title: Mapped[str] = mapped_column(
        String(255),
    )
    artist: Mapped[Optional[str]] = mapped_column(
        String(255),
    )
    file_name: Mapped[str] = mapped_column(
        String(40),
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    modified_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    )
