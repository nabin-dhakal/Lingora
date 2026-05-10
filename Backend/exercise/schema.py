from pydantic import BaseModel
from typing import List
from datetime import datetime


class ExerciseBase(BaseModel):
    title: str
    content: str
    lesson_id: str


class ExerciseSchema(ExerciseBase):
    id: int

    class Config:
        from_attributes = True