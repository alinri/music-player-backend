from fastapi import APIRouter

from . import auth, music, playlist, playlist_track, user

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(auth.router)
router.include_router(music.router)
router.include_router(playlist.router)
router.include_router(playlist_track.router)
