from fastapi import FastAPI
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from user.url import Router as UserRouter
from langs.urls import router as LangsRouter
from course.urls import router as CourseRouter
from lesson.urls import router as LessonRouter
from exercise.urls import router as ExerciseRouter
from demo.demo import router as DemoRouter
from core.database import Base, engine
from user import models

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redocs" if settings.DEBUG else None,
    openapi_url="/openapi.json" if settings.DEBUG else None
)

Base.metadata.create_all(bind=engine)

app.include_router(UserRouter, tags=["User"])
app.include_router(LangsRouter, tags=["Languages"])
app.include_router(CourseRouter, tags=["Courses"])
app.include_router(LessonRouter, tags=["Lessons"])
app.include_router(ExerciseRouter, tags=["Exercises"])
app.include_router(DemoRouter, tags=["Demo"])

@app.get('/')
async def root():
    return {
        "message": "Lingora - A Language Learning Platform",
        "version": settings.VERSION,
        "database": settings.DATABASE_URL,
        "debug": settings.DEBUG
    }