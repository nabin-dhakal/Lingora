from fastapi import  Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
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
        raise HttpException(status_code=404, detail="Courses not found")
    return courses


@router.get('/{course_id}', response_model=CourseSchema)
async def get_course(course_id: str, db: Session = Depends(get_db)) -> Course:
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
