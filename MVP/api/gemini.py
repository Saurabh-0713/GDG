from fastapi import APIRouter
import openai

router = APIRouter()

# Replace 'your-gemini-api-key' with the actual API key
GEMINI_API_KEY = "your-gemini-api-key"

@router.post("/ask_gemini/")
async def ask_gemini(question: str):
    """
    Uses Gemini AI to provide real-time insights for drug discovery.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}],
        api_key=GEMINI_API_KEY
    )

    return {"response": response['choices'][0]['message']['content']}
