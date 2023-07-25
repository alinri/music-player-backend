from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infra.repo.interface.music import IMusicRepo
from app.models.domain.music import Music


class MusicRepo(IMusicRepo):
    def __init__(self, session: Session):
        self._session = session

    def get_by_music_id(self, music_id: int) -> Music | None:
        stmt = select(Music).where(
            Music.music_id == music_id,
        )
        return self._session.scalars(stmt).first()

    def get_by_user_id(self, user_id: int) -> list[Music]:
        stmt = stmt = select(Music).where(
            Music.user_id == user_id,
        )
        return self._session.scalars(stmt).all()

    def insert(self, new_music: Music):
        self._session.add(new_music)
        self._session.commit()
