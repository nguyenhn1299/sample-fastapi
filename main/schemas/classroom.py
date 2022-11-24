from pydantic import BaseModel


class ClassroomCreateSchema(BaseModel):
    name: str
    floor: int
    capacity: int


class ClassroomSchema(BaseModel):
    class Config:
        orm_config = True
