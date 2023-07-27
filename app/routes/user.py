from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infra.dependencies import db_session
from app.infra.repo.sqlalchemy.user import UserRepo
from app.models.scheme.user.new_user import NewUserScheme
from app.usecase.user.new import NewUserUsecase

router = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
)
def register_user(
    new_user: NewUserScheme,
    session: Session = Depends(db_session),
):
    new_user_usecase = NewUserUsecase(UserRepo(session))
    new_user_usecase.execute(new_user)
