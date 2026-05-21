from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.chat_route import router

# Create App
app = FastAPI(
    title="Personal Agentic AI Chatbot",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Routes
app.include_router(router)


# Home Route
@app.get("/")
def home():

    return {
        "message": "Backend Running Successfully"
    }