import os
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from PIL import Image
from uuid import uuid4

router = APIRouter(prefix="/posts", tags=["Posts"])
UPLOAD_DIR = "backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PostResponse)
async def create_post(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    location: str = Form(...),
    date: str = Form(...),
    contactName: str = Form(...),
    contact: str = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    if category not in ["lost", "found"]:
        raise HTTPException(status_code=400, detail="Category must be 'lost' or 'found'.")

    image_path = None
    if image:
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Invalid image format.")
        ext = os.path.splitext(image.filename)[1]
        filename = f"{uuid4()}{ext}"
        image_path = os.path.join("uploads", filename)
        full_path = os.path.join("backend", image_path)
        with Image.open(image.file) as img:
            img = img.convert("RGB")
            img.thumbnail((800, 800))
            img.save(full_path, quality=85)

    new_post = models.Post(
        title=title,
        description=description,
        category=category,
        location=location,
        date=date,
        contact_name=contactName,
        contact=contact,
        image_path=image_path
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=list[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).order_by(models.Post.created_at.desc()).all()
