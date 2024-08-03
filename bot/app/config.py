from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    """
    Database settings
    """

    redis_url: str = "redis://redis_server:6379/0"


class Settings(BaseSettings):
    """
    Main settings
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

    bot_token: str
    db: BaseSettings = DBSettings()


# Setup configuration
try:
    settings = Settings()
except ValidationError:
    pass
