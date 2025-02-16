import pytest
from src.image_analyzer import analyze_image

def test_analyze_image_returns_mock_answer():
    image_path = 'test_data/test_image.jpg'
    question = "What is in the image?"

    response = analyze_image(image_path, question)

    assert isinstance(response, str)

    assert "Stub response" in response  