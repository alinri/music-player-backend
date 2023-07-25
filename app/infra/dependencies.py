from app.infra.db.database import Database


def db_session():
    with Database.get_session() as session:
        yield session
