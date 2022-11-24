from sqlalchemy.orm import Session

from main.models.classroom import ClassroomModel


class ClassroomEngine:
    @staticmethod
    def get_list(db_session: Session):
        return db_session.query(ClassroomModel).all()

    @staticmethod
    def get_one(db_session: Session, _id: int):
        return db_session.query(ClassroomModel).filter(ClassroomModel.id == _id).first()

    @staticmethod
    def create(db_session: Session, name: str, floor: int, capacity: int):
        obj = ClassroomModel(
            name=name, floor=floor, capacity=capacity
        )
        db_session.add(obj)
        return obj
