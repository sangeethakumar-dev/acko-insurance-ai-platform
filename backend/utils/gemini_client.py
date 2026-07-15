from google import genai

from backend.utils.config import GEMINI_API_KEY


gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_content(prompt: str):

    try:
        response = gemini_client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        return (
            "Sorry! The AI service is currently busy. "
            "Please try again in a few moments."
        )