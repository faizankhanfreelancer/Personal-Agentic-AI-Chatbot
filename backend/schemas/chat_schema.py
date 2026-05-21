from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    provider: str
    model: str
    system_prompt: str


class ChatResponse(BaseModel):
    response: str