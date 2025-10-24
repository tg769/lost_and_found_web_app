from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

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

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("website_frontend.html", "r", encoding="utf-8") as f:
        return f.read()
