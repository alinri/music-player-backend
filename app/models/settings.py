from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URI: str
    SECRET_KEY: str
    ALGORITHM = "HS256"
    model_config = SettingsConfigDict(env_file=".env")
