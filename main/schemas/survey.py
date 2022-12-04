from typing import List, Optional

from pydantic import BaseModel, constr, conlist, root_validator

from main.enums import QuestionType
from main.schemas.common import OrmSchema, TimestampSchema

"""
Question DTO
"""
_QuestionOptionSchema = constr(max_length=128)


class _MultipleChoiceQuestionDataSchema(BaseModel):
    options: conlist(_QuestionOptionSchema, max_items=10)


class _BaseQuestionSchema(BaseModel):
    title: constr(max_length=255)
    type: QuestionType
    is_required: Optional[bool] = False
    data: Optional[_MultipleChoiceQuestionDataSchema]

    @root_validator
    def validate_question_data_by_type(cls, question):
        # Only question of type multiple choice requires data for options
        if question["type"] == QuestionType.MULTIPLE_CHOICE:
            if question.get("data") is None:
                raise ValueError(f"Question type '{QuestionType.MULTIPLE_CHOICE}' requires data")

        return question


# POST Question Request DTO
class CreateQuestionSchema(_BaseQuestionSchema):
    pass


# PUT Question Request DTO
class UpdateQuestionSchema(_BaseQuestionSchema):
    id: Optional[int]
    # Set required fields to be optional in PUT request
    title: Optional[constr(max_length=255)]
    type: Optional[QuestionType]


# GET Question Response DTO
class QuestionSchema(_BaseQuestionSchema, OrmSchema):
    pass


"""
Survey DTO
"""


class _BaseSurveySchema(BaseModel):
    title: constr(max_length=255)
    description: constr(max_length=1024)


# POST Survey Request DTO
class CreateSurveySchema(_BaseSurveySchema):
    questions: conlist(CreateQuestionSchema, max_items=10)


# PUT Survey Request DTO
class UpdateSurveySchema(_BaseSurveySchema):
    title: Optional[constr(max_length=255)]
    description: Optional[constr(max_length=1024)]
    questions: Optional[conlist(UpdateQuestionSchema, max_items=10)]


# GET Survey Response DTO
class SurveySchema(_BaseSurveySchema, TimestampSchema, OrmSchema):
    pass


# GET Survey Response DTO
class SurveyDetailSchema(SurveySchema):
    questions: conlist(QuestionSchema, max_items=10)
