from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key:")
print(api_key[:10] + "..." + api_key[-6:])

client = genai.Client(api_key=api_key)

print("\nAvailable Models:\n")

for model in client.models.list():
    print(model.name)