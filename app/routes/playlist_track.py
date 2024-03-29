from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infra.auth.authenticate import authenticate
from app.infra.dependencies import db_session
from app.infra.repo.sqlalchemy.music import MusicRepo
from app.infra.repo.sqlalchemy.playlist import PlayListRepo
from app.infra.repo.sqlalchemy.playlist_track import PlayListTrackRepo
from app.models.scheme.auth.token_data import TokenData
from app.models.scheme.playlist_track.new_playlist_track import (
    NewPlayListTrackScheme,
)
from app.usecase.playlist_track.delete import DeletePlayListTrackUsecase
from app.usecase.playlist_track.new import NewPlayListTrackUsecase

router = APIRouter(prefix="/playlist-track", tags=["play list track"])


@router.post(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(authenticate)],
)
def new_playlist_track(
    new_track: NewPlayListTrackScheme,
    session: Annotated[Session, Depends(db_session)],
):
    new_playlist_track_usecase = NewPlayListTrackUsecase(
        PlayListTrackRepo(session),
        PlayListRepo(session),
        MusicRepo(session),
    )
    new_playlist_track_usecase.execute(
        new_track,
    )


@router.delete(
    "/{track_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_playlist_track(
    track_id: int,
    token_data: Annotated[TokenData, Depends(authenticate)],
    session: Annotated[Session, Depends(db_session)],
):
    delete_playlist_track = DeletePlayListTrackUsecase(
        PlayListTrackRepo(session),
        PlayListRepo(session),
    )
    delete_playlist_track.execute(track_id, token_data.user_id)
