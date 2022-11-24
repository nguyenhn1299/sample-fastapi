from sqlalchemy import Column, String, Integer

from main.database import BaseModel
from main.models.common import TimestampMixin


class ClassroomModel(BaseModel, TimestampMixin):
    name = Column(String, nullable=False)
    floor = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
