from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from sqlalchemy import Column, String, DateTime, Boolean
from core.database import Base

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

class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    category = Column(String, nullable=True)
    frequency = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Vocabulary(word={self.word}, lesson_id={self.lesson_id})>"
    
    def __str__(self):
        return self.word
    
class Sentence(Base):
    __tablename__ = "sentences"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    en = Column(String, nullable=False)
    sa = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    is_used = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    