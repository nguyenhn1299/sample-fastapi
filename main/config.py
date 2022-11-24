import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class Config:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Sample Project")
    CORS_ORIGINS: List[str] = [
        os.getenv("FRONTEND_ADDRESS", "http://localhost"),
        "http://localhost:3000",
        "*"
    ]

    # Postgres DB information
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT"))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URL: str = "postgresql://{}:{}@{}:{}/{}".format(
        os.getenv("POSTGRES_USER"),
        os.getenv("POSTGRES_PASSWORD"),
        os.getenv("POSTGRES_SERVER"),
        os.getenv("POSTGRES_PORT"),
        os.getenv("POSTGRES_DB"),
    )


config = Config()
