from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infra.auth.authenticate import authenticate
from app.infra.dependencies import db_session
from app.infra.repo.sqlalchemy.music import MusicRepo
from app.models.scheme.auth.token_data import TokenData
from app.models.scheme.music.music_out import MusicOutScheme
from app.models.scheme.music.new_music import NewMusicScheme
from app.usecase.music.list import ListMusicUsecase
from app.usecase.music.new import NewMusicUsecase

router = APIRouter(prefix="/music", tags=["music"])


@router.post(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def new_music(
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


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[MusicOutScheme],
)
def list_user_music(
    token_data: Annotated[TokenData, Depends(authenticate)],
    session: Annotated[Session, Depends(db_session)],
):
    list_music_usecase = ListMusicUsecase(
        MusicRepo(session),
    )
    return list_music_usecase.execute(token_data.user_id)
