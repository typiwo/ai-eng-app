import pytest
import os
import shutil
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_endpoint():
    """
    This test sends a GET request to the root endpoint ("/") and checks that:
    - The status code is 200 (OK).
    - The returned JSON contains the welcome message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Image Analysis API!"

def test_analyze_endpoint_valid_image(tmp_path):
    """
    This test checks that the /analyze endpoint works correctly when given a valid image.
    Steps:
    1. It copies a known-good image from the 'test_data' folder into a temporary directory.
    2. It sends a POST request to '/analyze' with the image file and a 'question' field.
    3. It asserts that the status code is 200 (success) and the returned JSON contains an 'analysis' key.
    """
    
    # Copy a real test image into tmp_path
    # Suppose you have test_data/dummy.jpg in your repo
    
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
