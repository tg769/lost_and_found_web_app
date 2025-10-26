from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from src.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(20), nullable=False)   # "lost" or "found"
    location = Column(String(100))
    date = Column(String(20))
    contact_name = Column(String(100))
    contact = Column(String(100))
    image_path = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
