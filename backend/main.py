from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import models, database
from routes import posts

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Lost & Found API")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded images
app.mount("/uploads", StaticFiles(directory="backend/uploads"), name="uploads")

# Routes
app.include_router(posts.router)

@app.get("/")
def root():
    return {"message": "Lost & Found API running"}
