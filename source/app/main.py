import uvicorn
from fastapi import FastAPI

import models
from db import engine
from db import SessionLocal
from core.config import settings
from schemas import User

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users/", response_model=User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.API_HOST,
        port=settings.API_PORT,
        debug=settings.DEBUG,
        log_level="info",
        reload=settings.RELOAD
    )