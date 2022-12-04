from sqlalchemy.orm import Session, Query

from main.schemas.common import GetPageSchema


class Engine:
    @staticmethod
    def paginate(query: Query, page: int, per_page: int):
        return GetPageSchema(
            page=page,
            per_page=per_page,
            items=query.offset((page - 1) * per_page).limit(per_page).all(),
            total=query.count(),
        )

