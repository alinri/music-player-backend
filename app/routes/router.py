from fastapi import APIRouter

from . import auth, music, playlist, user

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(auth.router)
router.include_router(music.router)
router.include_router(playlist.router)
