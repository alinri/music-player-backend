from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URI: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    origins: list[str]
    model_config = SettingsConfigDict(env_file=".env")
