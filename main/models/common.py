from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, String


class PersonMixin:
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)


class TimestampMixin:
    created = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated = Column(
        DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False
    )
