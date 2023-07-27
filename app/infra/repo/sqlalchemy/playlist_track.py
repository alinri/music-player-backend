from sqlalchemy import desc, select
from sqlalchemy.orm import Session, joinedload

from app.infra.repo.interface.playlist_track import IPlayListTrackRepo
from app.models.domain.playlist_track import PlayListTrack


class PlayListTrackRepo(IPlayListTrackRepo):
    def __init__(self, session: Session) -> None:
        self._session = session

    def insert(
        self,
        new_track: PlayListTrack,
    ):
        self._session.add(
            new_track,
        )
        self._session.commit()

    def list_by_playlist_id(
        self,
        playlist_id: int,
    ) -> list[PlayListTrack]:
        stmt = (
            select(PlayListTrack)
            .where(
                PlayListTrack.playlist_id == playlist_id,
            )
            .order_by(
                PlayListTrack.index,
            )
            .options(joinedload(PlayListTrack.music))
        )
        return self._session.scalars(stmt).all()

    def get_last_playlist_track(
        self,
        playlist_id: int,
    ) -> PlayListTrack | None:
        stmt = (
            select(PlayListTrack)
            .where(
                PlayListTrack.playlist_id == playlist_id,
            )
            .order_by(
                desc(PlayListTrack.index),
            )
        )
        return self._session.scalars(stmt).first()
