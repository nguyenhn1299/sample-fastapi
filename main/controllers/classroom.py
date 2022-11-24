from fastapi import APIRouter, Depends

from main.database import get_db
from main.schemas.classroom import ClassroomCreateSchema
from main.services.classroom import ClassroomService

router = APIRouter(prefix="/classrooms")


@router.get("")
def get_classrooms(
    db=Depends(get_db)
):
    srv = ClassroomService(db)
    return srv.get_classrooms()


@router.get("/{classroom_id}")
def get_classroom(
    classroom_id: int,
    db=Depends(get_db),
):
    srv = ClassroomService(db)
    return srv.get_classroom(_id=classroom_id)


@router.post("")
def create_classroom(
    classroom: ClassroomCreateSchema,
    db=Depends(get_db),
):
    srv = ClassroomService(db)
    return srv.create_classroom(classroom=classroom)
