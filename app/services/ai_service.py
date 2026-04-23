from openai import OpenAI
from app.core.config import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_ai_response(user_message: str):
    # prompt = f"""You are a friendly and helpful AI assistant for Ifa Homestay. Please answer the user's questions honestly and politely.

    # User message: {user_message}
    # """

    prompt = f"""You are a hotel assistant for LuxeSaty Pro.
    
    Helps Users with:
    - Room Booking
    - Room Availability
    - Hotel Services
    - Food Menu
    
    User: {user_message}

    """


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are helpful hote assistant. If you don't know the answer to any question, say I don't know."},
            {"role": "user", "content": user_message }
        ]
    )
    # if response.choices[0].message:
    #     return response.choices[0].message.content
    # return "Sorry, I couldn't understand that. Could you please rephrase your question?"

    return response.choices[0].message.content