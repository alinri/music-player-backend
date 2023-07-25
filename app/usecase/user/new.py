from fastapi import HTTPException, status

from app.infra.auth.password.hash import HashPassword
from app.infra.repo.interface.user import IUserRepo
from app.models.domain.user import User
from app.models.scheme.user.new_user import NewUserScheme


class NewUserUsecase:
    def __init__(
        self,
        user_repo: IUserRepo,
    ) -> None:
        self._user_repo = user_repo
        self._hash_password = HashPassword()

    def execute(
        self,
        new_user: NewUserScheme,
    ):
        username_exist = self._user_repo.get_by_username(
            new_user.username,
        )
        if username_exist:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail="نام کاربری تکراری",
            )
        hashed_password = self._hash_password.hash(
            new_user.password,
        )
        user = User(
            username=new_user.username,
            password=hashed_password,
            phone_number=new_user.phone_number,
            full_name=new_user.full_name,
        )
        self._user_repo.insert_user(user)
