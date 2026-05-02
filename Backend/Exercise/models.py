from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from sqlalchemy import Column, String, DateTime, Boolean
from Core.database import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=True)
    lesson_id = Column(String(36), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Exercise(question={self.question}, lesson_id={self.lesson_id})>"
    
    def __str__(self):
        return self.question
    