from passlib.context import CryptContext


class HashPassword:
    def __init__(self) -> None:
        self.context = CryptContext(schemes=["bcrypt"])

    def hash(self, plain_password: str) -> str:
        return self.context.hash(plain_password)
