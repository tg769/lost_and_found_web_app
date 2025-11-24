from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.routes import posts

import os

# Create the FastAPI app instance
app = FastAPI()

# CORS configuration to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to load the HTML frontend file
def load_frontend_html():
    file_path = os.path.join(os.path.dirname(__file__), "routes", "website_frontend.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Serve the index HTML file at the root route
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    return load_frontend_html()

# Include API routes
app.include_router(posts.router)

# Serve static files (e.g., uploaded images)
static_directory = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_directory, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_directory), name="static")
