import os
from PIL import Image
from src.llm import get_llm_response

def analyze_image(image_path: str, question: str) -> str:
    """
    A function that analyzes an image using Pillow and returns a response.
    In the future, this will integrate an actual LLM, but for now it's a mock.
    """

    # 1. Validate file path
    if not os.path.exists(image_path):
        raise ValueError(f"Invalid file path: {image_path}")

    # 2. Try opening the image with Pillow
    try:
        with Image.open(image_path) as img:
            image_format = img.format
            width, height = img.size
    except Exception:
        # If the file can't be opened as an image, raise an error
        raise ValueError(f"Invalid image file: {image_path}")
    
    # 3. Create a context string from the image info
    context = f"Image format: {image_format}, Size: {width}x{height}"

    # 4. Get the LLM response using our mock function
    llm_response = get_llm_response(question, context)

    return llm_response