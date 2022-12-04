from fastapi import APIRouter

from . import survey
from ..database import BaseModel, engine

BaseModel.metadata.create_all(bind=engine)

controller_router = APIRouter()


controller_router.include_router(survey.router, tags=["Surveys"])
