from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = None
    APP_NAME: str = "Begging Cup"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()

if not settings.DATABASE_URL:
    # In Production, use AWS Secrets Manager
    pass