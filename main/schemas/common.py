from datetime import datetime
from typing import Optional, List, TypeVar, Generic
from fastapi import Query

from pydantic import conint, BaseModel
from pydantic.generics import GenericModel

from main import config


T = TypeVar("T")


class TimestampSchema(BaseModel):
    created: datetime
    updated: datetime


class OrmSchema(BaseModel):
    # pass
    id: int

    class Config:
        orm_mode = True


class PaginationSchema(BaseModel):
    pass


class QueryParamsPageSchema(BaseModel):
    page: conint(gt=0) = 1
    per_page: conint(gt=0, le=100) = config.DEFAULT_PAGINATION_SIZE
    search: Optional[str] = Query(None)


class GetPageSchema(GenericModel, Generic[T]):
    page: conint(gt=0) = 1
    per_page: conint(gt=0, le=100) = config.DEFAULT_PAGINATION_SIZE
    items: List[T]
    total: conint(ge=0)

