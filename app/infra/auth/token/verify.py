from fastapi import HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt

from app.models.scheme.auth.token_data import TokenData
from app.models.settings import Settings


class AccessTokenVerify:
    def __init__(self) -> None:
        self._settings = Settings()

    def verify(
        self,
        token: str,
    ) -> TokenData:
        try:
            payload = jwt.decode(
                token,
                self._settings.SECRET_KEY,
                algorithms=[
                    self._settings.ALGORITHM,
                ],
            )
            token_data = TokenData.model_validate(payload)
        except ExpiredSignatureError:
            raise HTTPException(
                status.HTTP_403_FORBIDDEN,
                "نشست شما منقضی شده است.",
            )

        except JWTError:
            raise HTTPException(
                status.HTTP_403_FORBIDDEN,
                "دسترسی نامعتبر است.",
            )
        return token_data
