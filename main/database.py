from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr

from main import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_size=100, max_overflow=200
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class DeclarativeBaseModel:
    @declared_attr
    def __tablename__(cls):
        object_name = cls.__name__.replace("Model", "")
        return object_name.lower() + "s"

    id = Column(Integer, primary_key=True)


BaseModel = declarative_base(cls=DeclarativeBaseModel)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
