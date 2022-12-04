from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from main.database import get_db
from main.schemas.common import QueryParamsPageSchema, GetPageSchema
from main.schemas.survey import SurveySchema, SurveyDetailSchema, CreateSurveySchema, UpdateSurveySchema
from main.services.survey import SurveyService

router = APIRouter()


def _raise_not_found():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Survey not found",
    )


@router.post("/surveys", response_model=SurveyDetailSchema)
def create_survey(
    survey: CreateSurveySchema,
    db=Depends(get_db),
):
    return SurveyService(db).create_survey(survey)


@router.get("/surveys", response_model=GetPageSchema[SurveySchema])
def get_surveys(
    db=Depends(get_db),
    paging_params: QueryParamsPageSchema = Depends(),
):
    return SurveyService(db).get_surveys(paging_params)


@router.get("/surveys/{survey_id}", response_model=SurveyDetailSchema)
def get_survey(
    survey_id: int,
    db=Depends(get_db),
):
    survey = SurveyService(db).get_survey(survey_id)
    if not survey:
        _raise_not_found()
    return survey


@router.put("/surveys/{survey_id}", response_model=SurveyDetailSchema)
def update_survey(
    survey_id: int,
    survey: UpdateSurveySchema,
    db=Depends(get_db),
):
    survey = SurveyService(db).update_survey(survey_id, survey)
    if not survey:
        _raise_not_found()
    return survey


@router.delete("/surveys/{survey_id}")
def delete_survey(
    survey_id: int,
    db=Depends(get_db),
):
    SurveyService(db).delete_survey(survey_id)
