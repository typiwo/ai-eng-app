from fastapi import FastAPI, UploadFile, File, HTTPException, Form
import os

from src.image_analyzer import analyze_image

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Image Analysis API!"}

@app.post("/analyze")
async def analyze_endpoint(
    question: str = Form(...), 
    file: UploadFile = File(...)):
    """
    Endpoint to accept an image and a question, 
    then return the analysis as JSON.
    """
    # 1. Save the uploaded file temporarily
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as buffer:
        buffer.write(await file.read())

    # 2. Analyze it
    try:
        response = analyze_image(temp_filename, question)
    except ValueError as e:
        # If it's invalid, remove the file and return 400
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Clean up the file once we're done
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

    # 3. Return the response as JSON
    return {"analysis": response}
