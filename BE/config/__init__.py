from pydantic_settings import BaseSettings,SettingsConfigDict


class CommonSettings(BaseSettings):
    APP_NAME: str = "Evolink API"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URI: str
    OPEN_AI_KEY: str
    DB_NAME: str
    model_config = SettingsConfigDict(env_file=".env")



class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()