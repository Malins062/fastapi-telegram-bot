import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ApiV1Prefix(BaseModel):
    """
    Настройка API для версии 1
    """

    prefix: str = "/v1"
    messages: str = "/messages"
    message: str = "/message"


class Api(BaseModel):
    """
    Настройки API
    """

    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = os.getenv("PORT", 8000)


class DBSettings(BaseModel):
    """
    Настройки для баз данных
    """

    redis_url: str = os.getenv("REDIS", "redis://redis_server:6379/0")


class Settings(BaseSettings):
    """
    Основные настройки
    """

    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str = os.getenv("BOT_TOKEN")
    prefixes_command: str = os.getenv("PREFIXES_COMMAND", "!/\\")

    api: Api = Api()
    db: BaseSettings = DBSettings()


# Загрузка конфигурации
settings = Settings()
