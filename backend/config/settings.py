from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "").strip()

if not OPENAI_API_KEY:
    print("WARNING: OPENAI_API_KEY is not set in .env")
if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not set in .env")