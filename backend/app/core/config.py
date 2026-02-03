from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configurações globais da aplicação.
    Carregadas via variáveis de ambiente.
    """

    APP_NAME: str = "ANS Backend"
    ENV: str = "development"

    DATABASE_URL: str

    ETL_AUTO_RUN: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
