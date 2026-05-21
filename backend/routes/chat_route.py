from fastapi import APIRouter, HTTPException
import logging

from backend.schemas.chat_schema import (
    ChatRequest,
    ChatResponse,
)

from backend.agents.agent import run_agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


# Health Route
@router.get("/health")
def health_check():

    return {
        "status": "running"
    }


# Models Route
@router.get("/models")
def get_models():

    return {
        "openai": [
            "gpt-4o-mini",
            "gpt-4.1-mini"
        ],

        "groq": [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant"
]
    }


# Chat Route
@router.post("/chat")
def chat(request: ChatRequest):

    response = run_agent(
        message=request.message,
        provider=request.provider,
        model=request.model,
        system_prompt=request.system_prompt,
    )

    return ChatResponse(response=response)