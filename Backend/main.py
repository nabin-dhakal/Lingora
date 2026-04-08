from fastapi import FastAPI
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from user.url import Router as UserRouter


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redocs" if settings.DEBUG else None,
    openapi_url="/openapi.json" if settings.DEBUG else None
)


app.include_router(UserRouter, tags=["User"])

@app.get('/')
async def root():
    return {
        "message": "Lingora - A Language Learning Platform  ",
        "version": settings.VERSION,
        "database": settings.DATABASE_URL,
        "debug" : settings.DEBUG
    }
