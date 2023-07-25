from datetime import datetime, timedelta, timezone

from jose import jwt

from app.models.scheme.auth.token_data import TokenData
from app.models.settings import Settings


class AccessTokenSign:
    def __init__(self) -> None:
        self._settings = Settings()

    def sign(
        self,
        token_data: TokenData,
        expires_delta: timedelta = timedelta(
            days=30,
        ),
    ) -> str:
        claims = token_data.model_dump()
        expire = datetime.now(tz=timezone.utc) + expires_delta
        claims.update(
            {
                "exp": expire,
            },
        )

        encoded_jwt = jwt.encode(
            claims,
            self._settings.SECRET_KEY,
            self._settings.ALGORITHM,
        )
        return encoded_jwt
