from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from sqlalchemy import Column, String, DateTime, Boolean
from Core.database import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    course_id = Column(String(36), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Lesson(title={self.title}, course_id={self.course_id})>"
    
    def __str__(self):
        return self.title