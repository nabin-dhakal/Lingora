"""
Demo endpoints for mid-defense presentation
Shows translation exercise flow without database
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

# Create router
router = APIRouter(prefix="/demo", tags=["demo"])

# Hardcoded exercises (in-memory, no database)
EXERCISES = {
    1: {
        "id": 1,
        "english": "Hello",
        "sanskrit": "नमस्ते",
        "type": "translation"
    },
    2: {
        "id": 2,
        "english": "Thank you",
        "sanskrit": "धन्यवादः",
        "type": "translation"
    },
    3: {
        "id": 3,
        "english": "Water",
        "sanskrit": "जलम्",
        "type": "translation"
    },
    4: {
        "id": 4,
        "english": "Sun",
        "sanskrit": "सूर्यः",
        "type": "translation"
    },
    5: {
        "id": 5,
        "english": "Moon",
        "sanskrit": "चन्द्रः",
        "type": "translation"
    }
}


# Request/Response Models
class ExerciseResponse(BaseModel):
    id: int
    english: str
    type: str


class SubmitRequest(BaseModel):
    exercise_id: int
    user_answer: str


class SubmitResponse(BaseModel):
    correct: bool
    correct_answer: Optional[str] = None
    feedback: str
    user_answer: str


# API Endpoints
@router.get("/exercises", response_model=List[ExerciseResponse])
def get_exercises():
    """
    Returns all exercises WITHOUT showing the Sanskrit answers.
    Frontend uses this to display questions to the user.
    """
    exercises = []
    for ex in EXERCISES.values():
        exercises.append(ExerciseResponse(
            id=ex["id"],
            english=ex["english"],
            type=ex["type"]
        ))
    return exercises


@router.get("/exercises/{exercise_id}", response_model=ExerciseResponse)
def get_exercise(exercise_id: int):
    """
    Returns a single exercise without the answer.
    """
    if exercise_id not in EXERCISES:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    ex = EXERCISES[exercise_id]
    return ExerciseResponse(
        id=ex["id"],
        english=ex["english"],
        type=ex["type"]
    )


@router.post("/submit", response_model=SubmitResponse)
def submit_answer(request: SubmitRequest):
    """
    Validates user's answer against the correct Sanskrit translation.
    """
    if request.exercise_id not in EXERCISES:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    exercise = EXERCISES[request.exercise_id]
    correct_sanskrit = exercise["sanskrit"]
    user_answer = request.user_answer.strip()
    correct_answer = correct_sanskrit
    
    # Normalize both strings for comparison (remove spaces, trim)
    normalized_user = user_answer.replace(" ", "").strip()
    normalized_correct = correct_sanskrit.replace(" ", "").strip()
    
    # Check if answer is correct
    if normalized_user == normalized_correct:
        return SubmitResponse(
            correct=True,
            correct_answer=None,
            feedback=f"Correct! '{exercise['english']}' is {correct_sanskrit} in Sanskrit.",
            user_answer=user_answer
        )
    else:
        return SubmitResponse(
            correct=False,
            correct_answer=correct_sanskrit,
            feedback=f"Not quite. '{exercise['english']}' in Sanskrit is {correct_sanskrit}.",
            user_answer=user_answer
        )


@router.get("/ping")
def ping():
    """
    Simple health check to confirm demo routes are working.
    """
    return {"message": "Demo API is working!", "exercises_available": len(EXERCISES)}