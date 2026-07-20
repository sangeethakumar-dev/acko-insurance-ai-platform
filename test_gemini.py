from google import genai
from backend.utils.config import GEMINI_API_KEY
from backend.utils.config import GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)

try:
    response = client.models.generate_content(
        model="GEMINI_MODEL",   
        contents="Hello"
    )

    print("SUCCESS!")
    print(response.text)

except Exception as e:
    print("ERROR:")
    print(e)