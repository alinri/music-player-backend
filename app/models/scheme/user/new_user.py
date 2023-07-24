from pydantic import BaseModel, Field


class NewUserScheme(BaseModel):
    username: str = (Field(min_length=5, max_length=255),)
    password: str = Field(
        min_length=8,
    )
    phone_number: str = Field(
        max_length=11,
        min_length=11,
        pattern=r"\d+",
    )
    full_name: str = Field(
        max_length=255,
    )
