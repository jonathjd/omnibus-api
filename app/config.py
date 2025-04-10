from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Bible Knowledge Graph API"
    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str

    # Load from .env file
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
