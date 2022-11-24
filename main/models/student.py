from sqlalchemy.orm import relationship

from main.database import BaseModel
from main.models.common import PersonMixin, TimestampMixin


class StudentModel(BaseModel, PersonMixin, TimestampMixin):
    enrollments = relationship("EnrollmentModel")
