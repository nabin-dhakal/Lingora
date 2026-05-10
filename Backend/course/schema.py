from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CourseBase(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None

class CourseSchema(CourseBase):
    id: str

    class Config:
        from_attributes = True