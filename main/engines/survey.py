from typing import List, Optional, Dict

from sqlalchemy.orm import Session

from main.engines.common import Engine
from main.models.survey import SurveyModel, QuestionModel


class SurveyEngine(Engine):
    @classmethod
    def get_list(cls, db_session: Session, page: int, per_page: int):
        query = (
            db_session.query(SurveyModel)
            .order_by(SurveyModel.updated.desc())
        )

        return cls.paginate(query, page, per_page)

    @staticmethod
    def get_one(db_session: Session, _id: int) -> Optional[SurveyModel]:
        return db_session.query(SurveyModel).filter(SurveyModel.id == _id).first()

    @staticmethod
    def create(db_session: Session, title: str, description: str, question_orders: List[int]) -> SurveyModel:
        obj = SurveyModel(
            title=title,
            description=description,
            question_orders=question_orders,
        )
        db_session.add(obj)
        return obj


class QuestionEngine:
    @staticmethod
    def get_one(db_session: Session, _id: int):
        return db_session.query(QuestionModel).filter(QuestionModel.id == _id).first()

    @staticmethod
    def create(db_session: Session, survey_id: int, title: str, type: str, is_required: bool, data: Optional[Dict]) -> QuestionModel:
        obj = QuestionModel(
            survey_id=survey_id, title=title, type=type, is_required=is_required, data=data,
        )
        db_session.add(obj)
        return obj
