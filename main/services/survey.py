from typing import Optional

from sqlalchemy.orm import Session

from main.engines.survey import SurveyEngine, QuestionEngine
from main.enums import QuestionType
from main.models.survey import SurveyModel, QuestionModel
from main.schemas.common import QueryParamsPageSchema
from main.schemas.survey import CreateSurveySchema, UpdateSurveySchema, CreateQuestionSchema, UpdateQuestionSchema


class SurveyService:
    def __init__(self, db_session: Session):
        self._db_session = db_session

    def _get_question(self, _id: int, survey_id: int) -> Optional[QuestionModel]:
        db_question = QuestionEngine.get_one(self._db_session, _id=_id)
        if db_question.survey_id != survey_id:
            return
        return db_question

    def _create_question(self, survey_id: int, question: CreateQuestionSchema):
        return QuestionEngine.create(
            db_session=self._db_session,
            survey_id=survey_id,
            title=question.title,
            type=question.type.value,
            is_required=question.is_required,
            data=question.data.dict() if question.type == QuestionType.MULTIPLE_CHOICE else None,
        )

    def _update_question(self, survey_id: int, question: UpdateQuestionSchema):
        db_question = self._get_question(_id=question.id, survey_id=survey_id)
        if not db_question:
            return

        if question.type:
            db_question.type = question.type
        if question.title:
            db_question.title = question.title
        if question.is_required is not None:
            db_question.is_required = question.is_required
        if question.data and question.type == QuestionType.MULTIPLE_CHOICE:
            db_question.data = question.data.dict()

        return db_question

    def create_survey(self, survey: CreateSurveySchema) -> SurveyModel:
        db_survey = SurveyEngine.create(
            db_session=self._db_session,
            title=survey.title,
            description=survey.description,
            question_orders=[]
        )
        # Flush to get survey ids
        self._db_session.flush()

        db_survey.questions = []
        for question in survey.questions:
            db_question = self._create_question(survey_id=db_survey.id, question=question)
            db_survey.questions.append(db_question)

        # Flush to get question ids
        self._db_session.flush()

        db_survey.question_orders = [db_question.id for db_question in db_survey.questions]
        self._db_session.commit()
        return db_survey

    def get_survey(self, _id: int) -> Optional[SurveyModel]:
        db_survey = SurveyEngine.get_one(self._db_session, _id=_id)
        if not db_survey:
            return

        db_survey.questions = []
        for question_id in db_survey.question_orders:
            db_survey.questions.append(self._get_question(_id=question_id, survey_id=db_survey.id))
        return db_survey

    def get_surveys(self, paging_params: QueryParamsPageSchema):
        return SurveyEngine.get_list(
            self._db_session,
            page=paging_params.page,
            per_page=paging_params.per_page,
        )

    def update_survey(self, _id: int, survey: UpdateSurveySchema):
        db_survey = self.get_survey(_id)
        if not db_survey:  # Then no update occurs
            return

        if survey.title:
            db_survey.title = survey.title
        if survey.description:
            db_survey.description = survey.description

        db_survey.questions = []
        for question in survey.questions or []:
            # If question id is not provided, create new question
            if not question.id:  # Then create new question
                db_question = self._create_question(survey_id=db_survey.id, question=question)
            else:
                db_question = self._update_question(survey_id=db_survey.id, question=question)
                # If question id is not found, raise error
                if not db_question:
                    raise
            db_survey.questions.append(db_question)

        self._db_session.flush()

        new_question_orders = [q.id for q in db_survey.questions]
        for current_question_id in db_survey.question_orders:
            if current_question_id not in new_question_orders:
                current_question = self._get_question(survey_id=db_survey.id, _id=current_question_id)
                self._db_session.delete(current_question)

        db_survey.question_orders = new_question_orders
        self._db_session.commit()
        return db_survey

    def delete_survey(self, _id: int):
        db_survey = self.get_survey(_id)
        if db_survey:
            self._db_session.delete(db_survey)
            self._db_session.commit()
