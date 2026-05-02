from fastapi import HttppException, Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from Core.database import get_db
from .models import Course
from .schema import CourseSchema
from typing import List


router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[CourseSchema])
async def get_courses(db: Session = Depends(get_db)) -> List[Course]:
    courses = db.query(Course).all()
    if courses is None:
        raise HttppException(status_code=404, detail="Courses not found")
    return courses