import os
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from src import models, schemas, database
from PIL import Image # Used to compress/resize uploaded images
from uuid import uuid4 # Generates unique image filenames

# Creates a router for all endpoints that begin with /posts
router = APIRouter(prefix="/posts", tags=["Posts"])

# Directory where uploaded images are saved relative to where
# FastAPI is serving in directory
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Every request gets a database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create a post
@router.post("/", response_model=schemas.PostResponse)
async def create_post(
    # Form data fields sent from frontend
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
    # Validate Category
    if category not in ["lost", "found"]:
        raise HTTPException(status_code=400, detail="Category must be 'lost' or 'found'.")

    image_path = None
    # Handle image upload
    if image:
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Invalid image format.")
        # Generate Unique filename
        ext = os.path.splitext(image.filename)[1]
        filename = f"{uuid4()}{ext}"
        full_path = os.path.join(UPLOAD_DIR, filename)
        image_path = f"uploads/{filename}"
        # Open image, convert to RGB, compress and save
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
# Get all posts sorted by newest to first
@router.get("/", response_model=list[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).order_by(models.Post.created_at.desc()).all()
