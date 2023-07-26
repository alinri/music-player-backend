from pydantic import BaseModel, Field


class NewPlayListScheme(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=255,
    )
    description: str | None = Field(
        default="",
        min_length=1024,
    )
