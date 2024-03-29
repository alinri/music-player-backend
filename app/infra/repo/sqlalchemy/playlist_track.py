from sqlalchemy import delete, desc, select, update
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

    def delete_playlist_track(
        self,
        track_id: int,
    ):
        track = self.get_track_by_id(track_id)
        update_indexes_stmt = (
            update(PlayListTrack)
            .where(PlayListTrack.index > track.index)
            .values(index=PlayListTrack.index - 1)
        )
        stmt = delete(PlayListTrack).where(
            PlayListTrack.playlist_track_id == track_id
        )
        self._session.execute(stmt)
        self._session.execute(update_indexes_stmt)
        self._session.commit()

    def get_track_by_id(
        self,
        track_id: int,
    ) -> PlayListTrack | None:
        stmt = select(PlayListTrack).where(
            PlayListTrack.playlist_track_id == track_id
        )
        return self._session.execute(stmt).scalars().first()
