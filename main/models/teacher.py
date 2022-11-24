from sqlalchemy.orm import relationship

from main.database import BaseModel
from main.models.common import PersonMixin, TimestampMixin


class TeacherModel(BaseModel, PersonMixin, TimestampMixin):
    course_schedules = relationship("CourseScheduleModel", back_populates="teacher")
