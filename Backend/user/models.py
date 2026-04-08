from sqlalchemy import Column, Integer, String, UUID, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key= True, default = lambda : str(uuid.uuid4()), index=True)
    username = Column(String, unique=True, index= True, nullable=False)
    email = Column(String, unique=True, index= True, nullable=False)
    hashed_password = Column(String, nullable=False)

    fullname = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    avatar_url = Column(String, nullable=True)
    bio = Column(String, nullable=True)