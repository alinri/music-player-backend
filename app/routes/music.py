from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infra.auth.authenticate import authenticate
from app.infra.dependencies import db_session
from app.infra.repo.sqlalchemy.music import MusicRepo
from app.models.scheme.auth.token_data import TokenData
from app.models.scheme.music.new_music import NewMusicScheme
from app.usecase.music.new import NewMusicUsecase

router = APIRouter(prefix="/music", tags=["music"])


@router.post(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def login_user(
    new_music: Annotated[NewMusicScheme, Depends()],
    token_data: Annotated[TokenData, Depends(authenticate)],
    session: Annotated[Session, Depends(db_session)],
):
    new_music_usecase = NewMusicUsecase(
        MusicRepo(session),
    )
    new_music_usecase.execute(
        new_music,
        token_data.user_id,
    )
