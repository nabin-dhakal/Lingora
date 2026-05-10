from fastapi import  Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from .models import Exercise
from .schema import ExerciseSchema, ExerciseListResponse, ExerciseSubmissionSchema, ExerciseSubmissionResponse
from typing import List


router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=ExerciseListResponse)
async def get_exercises(db: Session = Depends(get_db)) -> List[Exercise]:
    exercises = db.query(Exercise).all()
    if exercises is None:
        raise HTTPException(status_code=404, detail="Exercises not found")
    return {"exercises": exercises, "total": len(exercises)}


@router.get('/{exercise_id}', response_model=ExerciseSchema)
async def get_exercise(exercise_id: int, db: Session = Depends(get_db)) -> Exercise:
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise

@router.post('/exercises/{exercise_id}/submit', response_model=ExerciseSubmissionSchema)
async def submit_exercise(exercise_id: str, submission: ExerciseSubmissionSchema, db: Session = Depends(get_db)) -> ExerciseSubmissionResponse:
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    is_correct = submission.answer == "correct_answer"
    feedback = "Correct!" if is_correct else "Incorrect, try again."
    
    return ExerciseSubmissionResponse(exercise_id=exercise_id, is_correct=is_correct, feedback=feedback)