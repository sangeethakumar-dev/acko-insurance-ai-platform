from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.management.admin_chat_service import (
    admin_chat,
    get_admin_chat_history,
    clear_admin_history
)


router = APIRouter(
    prefix="/admin/chat",
    tags=["Admin AI Assistant"]
)


# REQUEST MODEL

class AdminChatRequest(BaseModel):
    question: str


# ADMIN CHAT

@router.post("/")
def chat(request: AdminChatRequest):

    try:

        return admin_chat(request.question)

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CHAT HISTORY

@router.get("/history")
def chat_history():

    try:

        return get_admin_chat_history()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CLEAR CHAT HISTORY

@router.delete("/history")
def clear_history():

    try:

        return clear_admin_history()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )