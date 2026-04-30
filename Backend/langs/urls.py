from fastapi import APIRouter

router = APIRouter(
    prefix="/langs",
    tags=["langs"],
    responses={404: {"description": "Not found"}},
)

