from pydantic import BaseModel
from pydantic_settings import BaseSettings

# from settings.env_config import (
#     SECRET_KEY,
#     ACCESS_TOKEN_EXPIRE_MINUTES,
#     SMTP_SERVER,
#     SMTP_PORT,
#     ALGORITHM,
#     SMTP_USERNAME,
#     SMTP_PASSWORD
# )


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/api"
    auth: str = "/auth"


class ApiPrefix(BaseModel):
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SMTP_SERVER: str
    SMTP_PORT: int
    ALGORITHM: str
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    FRONTED_URL: str

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
