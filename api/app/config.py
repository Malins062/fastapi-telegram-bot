from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    messages: str = "/messages"
    message: str = "/message"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    mongo_uri: str = "mongodb://localhost:27017/"
    mongo_db: str = "messages_fastapi"

    datetime_format: str = "%d.%m.%Y %H:%M:%S"
    pagination_count: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
