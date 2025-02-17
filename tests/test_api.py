import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Image Analysis API!"

def test_analyze_endpoint_valid_image(tmp_path):
    # Copy a real test image into tmp_path
    # Suppose you have test_data/dummy.jpg in your repo
    import shutil
    import os
    
    src_file = "test_data/test_image.JPG"
    dst_file = tmp_path / "image.jpg"
    shutil.copy(src_file, dst_file)

    with open(dst_file, "rb") as img_file:
        response = client.post(
            "/analyze",
            data={"question": "Is this a cat?"},
            files={"file": ("image.jpg", img_file, "image/jpeg")}
        )
    assert response.status_code == 200

def test_analyze_endpoint_invalid_file():
    # Fake text file pretending to be an image
    fake_data = b"This is not an image!"
    response = client.post(
        "/analyze",
        data={"question": "Fake?"},
        files={"file": ("fake.jpg", fake_data, "image/jpeg")}
    )
    assert response.status_code == 400
    assert "Invalid image file" in response.text
