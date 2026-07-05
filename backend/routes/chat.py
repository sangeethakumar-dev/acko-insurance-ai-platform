from fastapi import APIRouter
from pydantic import BaseModel
from google import genai

from backend.utils.config import GEMINI_API_KEY
from backend.rag.retrieval import retrieve_pipeline
from backend.rag.prompt_builder import build_prompt

router = APIRouter()

class ChatRequest(BaseModel):
    user_query: str

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

@router.post("/chat")
def chat(request: ChatRequest):
    user_query = request.user_query

    # Step 1: Retrieve relevant chunks
    top_3_chunks = retrieve_pipeline(user_query)

    # Step 2: Build prompt
    prompt = build_prompt(user_query, top_3_chunks)

    # Step 3: Send prompt to Gemini
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Step 4: Return response
    return {
        "user_query": user_query,
        "response": response.text
    }
