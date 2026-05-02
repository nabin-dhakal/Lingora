from fastapi import  Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from Core.database import get_db
from .models import Exercise
from .schema import ExerciseSchema
from typing import List


router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ExerciseSchema])
async def get_exercises(db: Session = Depends(get_db)) -> List[Exercise]:
    exercises = db.query(Exercise).all()
    if exercises is None:
        raise HTTPException(status_code=404, detail="Exercises not found")
    return exercises