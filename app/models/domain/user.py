from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.db.base import Base

if TYPE_CHECKING:
    from .music import Music


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(Text())
    phone_number: Mapped[Optional[str]] = mapped_column(String(11))
    full_name: Mapped[str] = mapped_column(String(255))
    musics: Mapped[list["Music"]] = relationship(back_populates="user")
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    modified_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    )
