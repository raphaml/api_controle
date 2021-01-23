from datetime import datetime

from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    price: int
    name: str
    description: str

class Item(UserBase):
    id: int
    name: str
    description: str
    price: int
    owner_id: int

    class Config:
        orm_mode = True