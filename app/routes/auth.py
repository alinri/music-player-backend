from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.infra.dependencies import db_session
from app.infra.repo.sqlalchemy.user import UserRepo
from app.models.scheme.auth.token import Token
from app.usecase.auth.login import LoginUsecase

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token", response_model=Token)
def register_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(db_session)],
):
    login_usecase = LoginUsecase(
        UserRepo(session),
    )
    return login_usecase.execute(
        form_data.username,
        form_data.password,
    )
