from dotenv import load_dotenv
import os
from google import genai


#Getting API_Key

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

#Gemini Client

gemini_client = genai.Client(
    api_key = api_key
)
