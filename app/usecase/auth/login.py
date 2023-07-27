from fastapi import HTTPException, status

from app.infra.auth.password.verify import VerifyPassword
from app.infra.auth.token.sign import AccessTokenSign
from app.infra.repo.interface.user import IUserRepo
from app.models.scheme.auth.token import Token
from app.models.scheme.auth.token_data import TokenData


class LoginUsecase:
    def __init__(
        self,
        user_repo: IUserRepo,
    ) -> None:
        self._user_repo = user_repo
        self._verify_passowrd = VerifyPassword()

    def execute(
        self,
        username: str,
        password: str,
    ) -> Token:
        user = self._user_repo.get_by_username(
            username,
        )

        if not user:
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED,
                "نام کاربری غلط می‌باشد.",
            )

        if self._verify_passowrd.verify(
            password,
            user.password,
        ):
            access_token_sign = AccessTokenSign()
            access_token = access_token_sign.sign(
                TokenData(
                    user_id=user.user_id,
                )
            )
            token = Token(
                access_token=access_token,
                token_type="bearer",
            )
            return token
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="کلمه عبور اشتباه می‌باشد.",
        )
