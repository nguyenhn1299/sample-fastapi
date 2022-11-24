from sqlalchemy.orm import Session

from main.engines.classroom import ClassroomEngine
from main.schemas.classroom import ClassroomCreateSchema


class ClassroomService:
    def __init__(self, db_session: Session):
        self._db_session = db_session
        self._engine = ClassroomEngine()

    def create_classroom(self, classroom: ClassroomCreateSchema):
        classroom = self._engine.create(
            db_session=self._db_session,
            name=classroom.name,
            floor=classroom.floor,
            capacity=classroom.capacity,
        )
        self._db_session.commit()
        return classroom

    def get_classroom(self, _id: int):
        return self._engine.get_one(self._db_session, _id=_id)

    def get_classrooms(self):
        return self._engine.get_list(self._db_session)
