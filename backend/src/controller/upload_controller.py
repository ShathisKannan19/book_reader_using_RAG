from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from src.services.upload_service import populate_database
import os
import logging
import shutil
router = APIRouter()

@router.post("/api/uploadfile")
async def create_file(file: UploadFile):
    # Create the directory if it doesn't exist
    os.makedirs("src/data", exist_ok=True)
    
    # Generate a unique filename (you might want to improve this)
    file_location = f"src/data/{file.filename}"
    
    # Save the file
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    populate_database()
    
    return JSONResponse(content={
        "filename": file.filename,
        "file_size": os.path.getsize(file_location),
        "file_path": file_location
    })