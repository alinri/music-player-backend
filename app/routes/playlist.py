from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infra.auth.authenticate import authenticate
from app.infra.dependencies import db_session
from app.infra.repo.sqlalchemy.playlist import PlayListRepo
from app.models.scheme.auth.token_data import TokenData
from app.models.scheme.playlist.new_playlist import NewPlayListScheme
from app.models.scheme.playlist.playlist_out import PlayListOutScheme
from app.usecase.playlist.list import ListPlayListUsecase
from app.usecase.playlist.new import NewPlayListUsecase

router = APIRouter(prefix="/playlist", tags=["play list"])


@router.post(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def new_playlist(
    new_music: NewPlayListScheme,
    token_data: Annotated[TokenData, Depends(authenticate)],
    session: Annotated[Session, Depends(db_session)],
):
    new_playlist_usecase = NewPlayListUsecase(
        PlayListRepo(session),
    )
    new_playlist_usecase.execute(
        new_music,
        token_data.user_id,
    )


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[PlayListOutScheme],
)
def list_playlist(
    token_data: Annotated[TokenData, Depends(authenticate)],
    session: Annotated[Session, Depends(db_session)],
):
    list_playlist_usecase = ListPlayListUsecase(
        PlayListRepo(session),
    )
    return list_playlist_usecase.execute(
        token_data.user_id,
    )
