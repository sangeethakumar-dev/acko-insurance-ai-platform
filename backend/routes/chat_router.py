from fastapi import APIRouter
from pydantic import BaseModel

from backend.utils.gemini_client import gemini_client
from backend.rag.retrieval import retrieve_pipeline
from backend.utils.prompt_builder import build_prompt
from backend.utils.intent_classifier import classify_intent

router = APIRouter()


class ChatRequest(BaseModel):
    user_query: str


@router.post("/chat")
def chat(request: ChatRequest):

    user_query = request.user_query

    # Step 1 : Detect Intent
    intent = classify_intent(user_query)

    # If it is a quote request
    if intent in ["bike", "car", "health"]:

        return {
            "user_query": user_query,
            "workflow":"quote",
            "insurance_type": intent,
            "message": f"{intent.capitalize()} insurance detected. Please fill the {intent.capitalize()} Insurance Quote form."
        }

    # Otherwise continue with Module 1 (RAG)

    top_3_chunks = retrieve_pipeline(user_query)

    prompt = build_prompt(user_query, top_3_chunks)

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "user_query": user_query,
        "intent": "general",
        "response": response.text
    }