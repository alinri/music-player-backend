from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URI: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    SMTP_PORT: int
    SMTP_PASSWORD: str
    SMTP_SENDER: str
    SMTP_SERVER: str
    origins: list[str]
    model_config = SettingsConfigDict(env_file=".env")
