from pydantic import BaseModel
from typing import List
from datetime import datetime

class LanguageBase(BaseModel):
    name: str
    code: str

class LanguageSchema(LanguageBase):
    id: int

    class Config:
        from_attributes = True