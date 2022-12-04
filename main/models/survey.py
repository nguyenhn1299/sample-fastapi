from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import relationship

from main.database import BaseModel
from main.models.common import TimestampMixin


class QuestionModel(BaseModel):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)

    survey_id = Column(
        Integer,
        ForeignKey("surveys.id", ondelete="CASCADE"),
        nullable=False
    )
    survey = relationship("SurveyModel")
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    is_required = Column(Boolean, nullable=False, default=False)
    data = Column(JSONB)


class SurveyModel(BaseModel, TimestampMixin):
    __tablename__ = "surveys"
    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    question_orders = Column(ARRAY(Integer))

