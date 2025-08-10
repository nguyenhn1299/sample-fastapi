from datetime import datetime
from typing import Optional, List, TypeVar, Generic, Annotated
from fastapi import Query

from pydantic import BaseModel, Field
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
    page: Annotated[int, Field(strict=True, gt=0)] = 1
    per_page: Annotated[int, Field(strict=True, gt=0, le=100)] = config.DEFAULT_PAGINATION_SIZE
    search: Optional[str] = Query(None)


class GetPageSchema(GenericModel, Generic[T]):
    page: Annotated[int, Field(strict=True, gt=0)] = 1
    per_page: Annotated[int, Field(strict=True, gt=0, le=100)] = config.DEFAULT_PAGINATION_SIZE
    items: List[T]
    total: Annotated[int, Field(strict=True, gt=0)]

