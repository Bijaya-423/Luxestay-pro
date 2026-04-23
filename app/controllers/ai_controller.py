from app.services.ai_service import get_ai_response
# from app.schemas.ai_schema import AIRequest

def chat_with_ai(data):
    reply = get_ai_response(data.message)

    return {
        "user_message": data.message,
        "ai_response": reply
    }
