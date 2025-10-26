from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os
from src import models, database
from src.routes import posts

models.Base.metadata.create_all(bind=database.engine)
# Creates the FastAPI instance
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
app.mount("/uploads", StaticFiles(directory="src/uploads"), name="uploads")

# Routes
app.include_router(posts.router)

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    file_path = os.path.join(os.path.dirname(__file__), "routes", "website_frontend.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
