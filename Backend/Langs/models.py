from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from sqlalchemy import Column, String, DateTime, Boolean
from Core.database import Base

class Language(Base):
    __tablename__ = "languages"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    code = Column(String(10), unique=True, index=True, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Language(name={self.name}, code={self.code})>"
    
    def __str__(self):
        return self.name
    
class Course(Base):
    __tablename__ = "courses"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    language_id = Column(String(36), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Course(title={self.title}, language_id={self.language_id})>"
    
    def __str__(self):
        return self.title
    
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
    
