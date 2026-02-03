from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"  # ignora qualquer variável extra


settings = Settings()
