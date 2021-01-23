from fastapi import FastAPI

from core.config import settings

import models
from db import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.API_HOST,
        port=settings.API_PORT,
        debug=settings.DEBUG,
        log_level="info",
        reload=settings.RELOAD
    )