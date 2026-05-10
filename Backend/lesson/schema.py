from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class LessonBase(BaseModel):
    title: str
    content: Optional[str] = None
    course_id: str

class LessonSchema(LessonBase):
    id: str

    class Config:
        from_attributes = True