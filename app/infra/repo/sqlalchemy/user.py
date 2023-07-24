from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infra.repo.interface.user import IUserRepo
from app.models.domain.user import User


class UserRepo(IUserRepo):
    def __init__(self, session: Session):
        self._session = session

    def get_by_username(self, username: str) -> User | None:
        stmt = select(User).where(
            User.username == username,
        )
        return self._session.scalars(stmt).first()

    def get_by_user_id(self, user_id: int) -> User | None:
        stmt = stmt = select(User).where(
            User.user_id == user_id,
        )
        return self._session.scalars(stmt).first()

    def insert_user(self, new_user: User):
        self._session.add(new_user)
        self._session.commit()
