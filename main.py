from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse
from PIL import Image
import uvicorn
import yolo_helper

app = FastAPI()

def is_valid_image(file):
    try:
        # Attempt to open the image using Pillow to validate its format
        Image.open(io.BytesIO(file))
        return True
    except Exception as e:
        return False

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    # Validate image format
    #if not is_valid_image(file.file.read()):
    #    raise HTTPException(status_code=422, detail="Invalid image format")

    # Validate file size
    #if file.file.seek(0, 2) > 1000000:
    #    raise HTTPException(status_code=413, detail="File size exceeds the limit")

    # Process the image
    result = yolo_helper.detect_people(file.file)
    
    # Return the result as JSON
    return JSONResponse(content={"people_count": result})

@app.get("/health")
async def health_check():
    return {"Status": "OK"}
