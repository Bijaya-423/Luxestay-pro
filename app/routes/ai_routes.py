from fastapi import APIRouter, Depends
from app.schemas.ai_schema import AIRequest
from app.controllers import ai_controller

router = APIRouter()

@router.post('/chat')
def chat(data:AIRequest):
    return ai_controller.chat_with_ai(data)

# @router.get('/test')
# def test():
#     return {'message':'AI routes working'}