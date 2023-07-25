from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.models.scheme.auth.token_data import TokenData

from .token.verify import AccessTokenVerify

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def authenticate(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> TokenData:
    access_token_verify = AccessTokenVerify()
    return access_token_verify.verify(token)
