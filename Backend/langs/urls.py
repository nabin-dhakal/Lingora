from fastapi import APIRouter
from .models import Language, Course, Lesson, Exercise
from core.database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/langs",
    tags=["langs"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getlangs(reqest: Request, db: Session = Depends(get_db)) -> List[Language]:
    return db.query(Language).all()
    