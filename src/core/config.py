from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str = Field("0.0.0.0", env="SERVER_HOST")
    SERVER_PORT: int = Field(8080, env="SERVER_PORT")

    POSTGRES_DSN: str = Field(
        "postgresql+asyncpg://postgres:postgres@127.0.0.1/testdb1",
        env="POSTGRES_DSN")
    REDIS_DB_HOST: str = Field("localhost", env="REDIS_DB_HOST")
    REDIS_DB_PORT: int = Field(6379, env="REDIS_DB_PORT")
    REDIS_DB_NUM: int = Field(0, env="REDIS_DB_NUM")

    RABBITMQ_URL: str = Field("amqp://admin:admin@127.0.0.8/")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
assert True
