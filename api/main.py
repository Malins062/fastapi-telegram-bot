import uvicorn
from api.app.config import Settings
from api.app.routers import router
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI messages",
    description="Тестовое задание FastAPI",
)
app.include_router(router)

settings = Settings()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.run.host,
        port=settings.run.port,
        # reload=True,
    )
