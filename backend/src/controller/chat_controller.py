from fastapi import APIRouter, HTTPException, routing
from src.models.chat_model import ChatRequest
from src.services.chat_service import chat_service_response
import logging
router = APIRouter()

@router.post('/api/chat')
def chat_endpoint(request: ChatRequest):
    try:
        text = request.query
        
        resposne = chat_service_response(text)
        
        return {"response":resposne}

    except HTTPException as http_exc:
        raise http_exc
    
    except Exception as e:
        logging.error(f"Error processing chat request: {e}")
        raise HTTPException(status_code=500, detail=str(e))