import uvicorn
from fastapi import FastAPI

from api.app.config import Settings

app = FastAPI()

settings = Settings()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
