from sqlalchemy import Column, Integer, ForeignKey

# from main.models import StudentModel, CourseModel
from main.database import BaseModel


class EnrollmentModel(BaseModel):
    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )
    course_id = Column(
        Integer,
        ForeignKey("courses.id", ondelete="CASCADE"),
        nullable=False
    )
