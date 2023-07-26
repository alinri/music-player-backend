from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infra.repo.interface.playlist import IPlayListRepo
from app.models.domain.playlist import PlayList


class MusicRepo(IPlayListRepo):
    def __init__(
        self,
        session: Session,
    ):
        self._session = session

    def insert(
        self,
        new_playlist: PlayList,
    ):
        self._session.add(new_playlist)
        self._session.commit()

    def list_by_user_id(
        self,
        user_id: int,
    ) -> list[PlayList]:
        stmt = select(PlayList).where(PlayList.user_id == user_id)
        return self._session.scalars(stmt).all()
