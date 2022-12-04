from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr

from main import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_size=100, max_overflow=200
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


BaseModel = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
