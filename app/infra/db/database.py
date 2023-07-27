from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.infra.db.base import Base
from app.models.domain.music import Music
from app.models.domain.playlist_track import PlayListTrack
from app.models.domain.user import User


class Database:
    sessoin_maker: sessionmaker | None = None

    @classmethod
    def init(
        cls,
        uri: str,
    ):
        db_engine = create_engine(uri)
        cls.sessoin_maker = sessionmaker(bind=db_engine)
        Base.metadata.create_all(db_engine)

    @classmethod
    def get_session(
        cls,
    ) -> Session:
        return cls.sessoin_maker()
