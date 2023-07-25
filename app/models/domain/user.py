from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.infra.db.base import Base


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(Text())
    phone_number: Mapped[Optional[str]] = mapped_column(String(11))
    full_name: Mapped[str] = mapped_column(String(255))
