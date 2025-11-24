import os
import io
from fastapi.testclient import TestClient
from PIL import Image

from src.main import app
from src import models, database

client = TestClient(app)


# Helpers to keep database clean

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def reset_database():
    """Clear all posts before each test"""
    db = next(get_db())
    db.query(models.Post).delete()
    db.commit()


#   Tests

def test_get_posts_initially_empty():
    reset_database()
    response = client.get("/posts/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_simple_post():
    reset_database()
    data = {
        "title": "Lost Wallet",
        "description": "Black leather wallet.",
        "category": "lost",
        "location": "Library",
        "date": "2025-10-26",
        "contactName": "Skit",
        "contact": "555-1234"
    }

    response = client.post("/posts/", data=data)
    assert response.status_code == 200

    body = response.json()
    assert body["title"] == "Lost Wallet"
    assert body["description"] == "Black leather wallet."
    assert body["category"] == "lost"
    assert body["location"] == "Library"
    assert body["date"] == "2025-10-26"
    assert body["contact_name"] == "Skit"
    assert body["contact"] == "555-1234"
    assert body["image_path"] is None


def test_create_post_with_image(tmp_path):
    reset_database()

    # Create a PIL image in memory
    img = Image.new("RGB", (50, 50), color="red")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    data = {
        "title": "Lost Keys",
        "description": "Blue keychain.",
        "category": "lost",
        "location": "Cafeteria",
        "date": "2025-10-26",
        "contactName": "Skit",
        "contact": "contact@example.com"
    }

    files = {"image": ("upload.png", img_bytes, "image/png")}

    response = client.post("/posts/", data=data, files=files)
    assert response.status_code == 200

    body = response.json()
    assert body["title"] == "Lost Keys"
    assert body["image_path"] is not None

    # Confirm image saved
    saved_path = os.path.join("src/uploads", os.path.basename(body["image_path"]))
    assert os.path.exists(saved_path)

    # Cleanup
    os.remove(saved_path)


def test_invalid_file_rejected():
    reset_database()
    data = {
        "title": "Lost Phone",
        "description": "Silver case.",
        "category": "lost",
        "location": "Office",
        "date": "2025-10-26",
        "contactName": "Skit",
        "contact": "111-2222"
    }

    files = {"image": ("malware.txt", b"fakecontent", "text/plain")}

    response = client.post("/posts/", data=data, files=files)
    assert response.status_code == 400


def test_database_content():
    reset_database()

    data = {
        "title": "iPad",
        "description": "White",
        "category": "lost",
        "location": "Lobby",
        "date": "2025-10-26",
        "contactName": "Skit",
        "contact": "222-2222"
    }

    client.post("/posts/", data=data)

    response = client.get("/posts/")
    body = response.json()
    assert len(body) == 1
    assert body[0]["title"] == "iPad"
