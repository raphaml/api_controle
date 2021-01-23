import uvicorn
from fastapi import FastAPI


import models
from db import engine
from core.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.API_HOST,
        port=settings.API_PORT,
        debug=settings.DEBUG,
        log_level="info",
        reload=settings.RELOAD
    )