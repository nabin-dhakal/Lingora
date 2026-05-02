from fastapi.routing import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from Core.database import get_db
from .models import Lesson
from .schema import LessonSchema
from typing import List

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[LessonSchema])
async def get_lessons(db: Session = Depends(get_db)) -> List[Lesson]:
    lessons = db.query(Lesson).all()
    if lessons is None:
        raise HTTPException(status_code=404, detail="Lessons not found")
    return lessons