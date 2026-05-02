from pydantic import BaseModel
from typing import List
from datetime import datetime

class LessonBase(BaseModel):
    title: str
    content: str
    course_id: str

class LessonSchema(LessonBase):
    id: int

    class Config:
        from_attributes = True