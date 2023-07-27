from passlib.context import CryptContext


class VerifyPassword:
    def __init__(self) -> None:
        self.context = CryptContext(schemes=["bcrypt"])

    def verify(
        self,
        plain_password: str,
        hashed_password: str,
    ) -> bool:
        return self.context.verify(
            plain_password,
            hashed_password,
        )
