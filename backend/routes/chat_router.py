from fastapi import APIRouter
from pydantic import BaseModel

from backend.utils.gemini_client import gemini_client
from backend.rag.retrieval import retrieve_pipeline
from backend.utils.prompt_builder import build_prompt
from backend.utils.intent_classifier import classify_intent
from backend.utils.config import GEMINI_MODEL

router = APIRouter()


class ChatRequest(BaseModel):
    user_query: str


@router.post("/chat")
def chat(request: ChatRequest):

    user_query = request.user_query

    # Step 1 : Detect Intent
    intent = classify_intent(user_query)

    # ==================General Greeting========================

    if intent == "greeting":

        response = gemini_client.models.generate_content(
        model="YOUR_WORKING_MODEL",
        contents=user_query
    )

        return {
        "user_query": user_query,
        "intent": "greeting",
        "response": response.text
    }

    # ================= QUOTATION =================

    if intent in ["bike", "car", "health"]:

        return {
            "user_query": user_query,
            "workflow": "quote",
            "insurance_type": intent,
            "message": f"Sure! I'll help you with your {intent.capitalize()} Insurance quotation. Please fill in the details below."
        }

    # ================= CLAIM =================

    if intent == "claim":

        return {
            "user_query": user_query,
            "workflow": "claim",
            "message": "Sure! Please upload the damage images and complete the claim form below."
        }

    # ================= GENERAL RAG =================

    try:
        top_3_chunks = retrieve_pipeline(user_query)

        prompt = build_prompt(user_query, top_3_chunks)

        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return {
            "user_query": user_query,
            "intent": "general",
            "response": response.text
        }

    except Exception as e:
        print("Chat Router Error:", e)

        return {
            "user_query": user_query,
            "intent": "general",
            "response": "Sorry! The AI service is temporarily busy. Please try again in a few moments."
        }