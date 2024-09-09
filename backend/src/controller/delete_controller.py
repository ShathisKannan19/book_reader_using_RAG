from fastapi import APIRouter, HTTPException, routing
from src.models.chat_model import ChatRequest
from src.services.upload_service import clear_database
import logging
router = APIRouter()

@router.delete("/api/clear_data")
def delete_chroma():
    try:
        clear_database()
        return {"response":"Cleared Data Base, Create fresh ✅"}
    except Exception as e:
        return f"An error occured mentioned below {e}"