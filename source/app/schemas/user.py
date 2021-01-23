from datetime import datetime

from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    hashed_password: str
    name: str
    created_at: datetime
    is_active: bool

class User(UserBase):
    id: int
    email: str
    hashed_password: str
    name: str
    created_at: datetime
    is_active: bool

    class Config:
        orm_mode = True