from pydantic import BaseModel
from typing import Optional, List

class ExerciseSchema(BaseModel):
    id: str
    question: str
    type: str
    order_index: int
    choices: Optional[str] = None
    lesson_id: str

    class Config:
        from_attributes = True


class ExerciseListResponse(BaseModel):
    exercises: List[ExerciseSchema]
    total: int


class ExerciseSubmissionSchema(BaseModel):
    answer: str


class ExerciseSubmissionResponse(BaseModel):
    exercise_id: str
    is_correct: bool
    feedback: Optional[str] = None