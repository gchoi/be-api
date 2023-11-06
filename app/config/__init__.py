from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STR: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()
