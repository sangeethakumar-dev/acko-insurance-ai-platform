from dotenv import load_dotenv
import os


#Getting API_Key

load_dotenv()

GEMINI_API_KEY  = os.getenv("GEMINI_API_KEY")