# from openai import OpenAI
# from app.core.config import settings


# client = OpenAI(api_key=settings.OPENAI_API_KEY)

# def get_ai_response(user_message: str):
#     # prompt = f"""You are a friendly and helpful AI assistant for Ifa Homestay. Please answer the user's questions honestly and politely.

#     # User message: {user_message}
#     # """

#     prompt = f"""You are a hotel assistant for LuxeSaty Pro.
    
#     Helps Users with:
#     - Room Booking
#     - Room Availability
#     - Hotel Services
#     - Food Menu
    
#     User: {user_message}

#     """


#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are helpful hote assistant. If you don't know the answer to any question, say I don't know."},
#             {"role": "user", "content": user_message }
#         ]
#     )
#     # if response.choices[0].message:
#     #     return response.choices[0].message.content
#     # return "Sorry, I couldn't understand that. Could you please rephrase your question?"

#     return response.choices[0].message.content


import requests

# ollama launch claude
# ollama launch codex

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_ai_response(user_message: str):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": f"You are a hotel assistant. {user_message}",
                "stream": False
            },
            timeout=30
        )
        if response.status_code != 200:
            return f"Ollama error: {response.text}"

        data = response.json()
        #fix: check full response
        print("Ollama Response:", data)

        # return data.get("response", "No response from AI")
        return data.get("response") or "AI returned empty response"
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"
        
