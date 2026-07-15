from google import genai

from backend.utils.config import GEMINI_API_KEY


gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_content(prompt: str):

    response = gemini_client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    return response.text
