from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_HOST: str 
    DB_PORT: str 
    DB_DATABASE: str 
    
    
    TELEGRAM_BOT_TOKEN: SecretStr
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()