from fastapi import FastAPI
from Core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from User.url import Router as UserRouter
from Langs.urls import router as LangsRouter
from Core.database import Base, engine
from User import models

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

@app.get('/')
async def root():
    return {
        "message": "Lingora - A Language Learning Platform",
        "version": settings.VERSION,
        "database": settings.DATABASE_URL,
        "debug": settings.DEBUG
    }