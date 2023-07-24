from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class Database:
    sessoin_maker: sessionmaker = None

    @classmethod
    def init(
        cls,
        uri: str,
    ):
        db_engine = create_engine(uri)
        cls.sessoin_maker = sessionmaker(bind=db_engine)

    @classmethod
    def get_session(
        cls,
    ) -> Session:
        return cls.sessoin_maker()
