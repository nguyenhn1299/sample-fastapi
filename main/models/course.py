from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from main.database import BaseModel
from main.models.classroom import ClassroomModel
from main.models.common import TimestampMixin
from main.models.teacher import TeacherModel


class CourseModel(BaseModel, TimestampMixin):
    name = Column(String, nullable=False)

    started = Column(DateTime)
    ended = Column(DateTime)

    schedules = relationship("CourseScheduleModel", back_populates="course")


class CourseScheduleModel(BaseModel):
    day_of_week = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)

    course_id = Column(
        Integer,
        ForeignKey(CourseModel.id, ondelete="CASCADE"),
        nullable=False
    )
    course = relationship("CourseModel", back_populates="schedules")

    teacher_id = Column(
        Integer,
        ForeignKey(TeacherModel.id, ondelete="SET NULL"),
    )
    teacher = relationship("TeacherModel")

    classroom_id = Column(
        Integer,
        ForeignKey(ClassroomModel.id, ondelete="SET NULL"),
    )
    classroom = relationship("ClassroomModel")
