from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    description: str
    category: str
    location: str
    date: str
    contact_name: str
    contact: str

class PostResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: Optional[str]
    date: Optional[str]
    contact_name: Optional[str]
    contact: Optional[str]
    image_path: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
