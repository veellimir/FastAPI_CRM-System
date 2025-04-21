from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/api/v1"

    auth: str = "/auth"
    users: str = "/users"
    role: str = "/user-role"
    news: str = "/news"


class ApiPrefix(BaseModel):
    v1: ApiV1Prefix = ApiV1Prefix()

    @property
    def bearer_token_url(self) -> str:
        parts = (self.v1.prefix, self.v1.auth, "/login")
        return "".join(parts)


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class MediaPath(BaseSettings):
    MEDIA_FOLDER_PROFILE: str


class DataBase(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int


class Settings(BaseSettings):
    SECRET_KEY: str

    FRONTEND_URL: str

    SMTP_EMAIL_HOST_USER: str
    SMTP_EMAIL_HOST_PASSWORD: str
    SMTP_EMAIL_HOST: str
    SMTP_EMAIL_PORT: int

    ACCESS_TOKEN_LIFETIME_SECONDS: int
    RESET_PASSWORD_TOKEN_SECRET: str
    VERIFICATION_PASSWORD_TOKEN_SECRET: str

    SUPER_USER_EMAIL: str
    SUPER_USER_PASSWORD: str
    SUPER_USER_IS_ACTIVE: bool
    SUPER_USER_IS_SUPERUSER: bool
    SUPER_USER_IS_VERIFIED: bool

    db: DataBase = DataBase()
    media: MediaPath = MediaPath()

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

    @property
    def access_token(self) -> AccessToken:
        return AccessToken(
            reset_password_token_secret=self.RESET_PASSWORD_TOKEN_SECRET,
            verification_token_secret=self.VERIFICATION_PASSWORD_TOKEN_SECRET,
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


settings = Settings()
