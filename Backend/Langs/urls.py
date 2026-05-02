from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from Core.database import get_db
from .models import Language
from .schema import LanguageSchema

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[LanguageSchema])
async def get_language(db: Session = Depends(get_db)) -> List[Language]:
    lang = db.query(Language).all()
    if lang is None:
        raise HTTPException(status_code=404, detail="Languages not found")
    return lang



@router.get("/{lang_id}", response_model=LanguageSchema)
async def get_language(lang_id: int, db: Session = Depends(get_db)) -> Language:
    lang = db.query(Language).filter(Language.id == lang_id).first()
    if lang is None:
        raise HTTPException(status_code=404, detail="Language not found")
    return lang