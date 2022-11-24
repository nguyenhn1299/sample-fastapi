from datetime import datetime

from sqlalchemy import Column, DateTime, String


class PersonMixin:
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)


class TimestampMixin:
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
