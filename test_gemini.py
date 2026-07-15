from google import genai
from backend.utils.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

try:
    response = client.models.generate_content(
        model="gemini-flash-latest",   # You can also try gemini-2.5-flash
        contents="Hello"
    )

    print("SUCCESS!")
    print(response.text)

except Exception as e:
    print("ERROR:")
    print(e)