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
    
