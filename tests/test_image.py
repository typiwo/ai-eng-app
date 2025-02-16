import pytest
import os
from src.image_analyzer import analyze_image

def test_analyze_image_returns_non_empty_string():
    # Arrange
    image_path = os.path.join("test_data", "test_image.JPG")
    question = "What is in this image?"

    # Act
    response = analyze_image(image_path, question)

    # Assert
    assert isinstance(response, str), "The response should be a string"
    assert len(response) > 0, "The response string shouldn't be empty"

def test_analyze_image_invalid_path():
    # Arrange
    invalid_path = "test_data/this_file_does_not_exist.jpg"
    question = "Is this a cat?"

    # Act & Assert
    # We expect some exception or some handling of invalid path.
    # For now, let's say we expect a ValueError from our function:
    with pytest.raises(ValueError):
        analyze_image(invalid_path, question)