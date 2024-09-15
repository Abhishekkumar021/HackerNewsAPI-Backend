from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_HN_URL: str = ""
    Origin: str = "*"
    Allow_Methods: str = "*"

    class Config:
        env_file = ".env"


settings = Settings()

