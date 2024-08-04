import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

load_dotenv()


class RunConfig(BaseModel):
    """
    Настройки запуска сервера
    """

    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = os.getenv("PORT", 8000)


class ApiV1Prefix(BaseModel):
    """
    Настройка API для версии 1
    """

    prefix: str = "/v1"
    messages: str = "/messages"
    message: str = "/message"


class ApiPrefix(BaseSettings):
    """
    Настройки API
    """

    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseSettings):
    """
    Настройки БД
    """

    mongo_uri: str = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    mongo_db: str = os.getenv("MONGO_DB", "messages_fastapi")

    datetime_format: str = "%d.%m.%Y %H:%M:%S"
    pagination_count: int = 10


class Settings(BaseSettings):
    """
    Основные настройки
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()


# Установка конфигурации
settings = Settings()
