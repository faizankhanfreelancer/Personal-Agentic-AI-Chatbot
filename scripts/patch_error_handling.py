from pathlib import Path

patches = [
    (
        Path("backend/config/settings.py"),
        "# Load .env file\nload_dotenv()\n\n# API Keys\nOPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\")\nGROQ_API_KEY = os.getenv(\"GROQ_API_KEY\")\nTAVILY_API_KEY = os.getenv(\"TAVILY_API_KEY\")\n",
        "# Load .env file\nload_dotenv()\n\nOPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\", \"\").strip()\nGROQ_API_KEY = os.getenv(\"GROQ_API_KEY\", \"\").strip()\nTAVILY_API_KEY = os.getenv(\"TAVILY_API_KEY\", \"\").strip()\n\nif not OPENAI_API_KEY:\n    print(\"WARNING: OPENAI_API_KEY is not set in .env\")\nif not GROQ_API_KEY:\n    print(\"WARNING: GROQ_API_KEY is not set in .env\")\n",
    ),
    (
        Path("backend/routes/chat_route.py"),
        "# Chat Route\n@router.post(\"/chat\")\ndef chat(request: ChatRequest):\n\n    response = run_agent(\n        message=request.message,\n        provider=request.provider,\n        model=request.model,\n        system_prompt=request.system_prompt,\n    )\n\n    return ChatResponse(response=response)\n",
        "# Chat Route\n@router.post(\"/chat\", response_model=ChatResponse)\ndef chat(request: ChatRequest):\n\n    try:\n        response = run_agent(\n            message=request.message,\n            provider=request.provider,\n            model=request.model,\n            system_prompt=request.system_prompt,\n        )\n\n        return ChatResponse(response=response)\n\n    except Exception as exc:\n        error_message = str(exc) or \"Unknown backend error\"\n        logger.exception(\"Error in /chat endpoint\")\n        raise HTTPException(status_code=500, detail=error_message)\n",
    ),
    (
        Path("frontend/app.py"),
        "    # Send API Request\n    with st.spinner(\"Thinking...\"):\n\n        response = requests.post(\n            API_URL,\n            json=payload\n        )\n\n        ai_response = response.json()[\"response\"]\n\n    # Store AI Response\n    st.session_state.messages.append(\n        {\n            \"role\": \"assistant\",\n            \"content\": ai_response\n        }\n    )\n\n    with st.chat_message(\"assistant\"):\n        st.markdown(ai_response)\n",
        "    # Send API Request\n    with st.spinner(\"Thinking...\"):\n\n        try:\n            response = requests.post(\n                API_URL,\n                json=payload,\n                timeout=30,\n            )\n            response.raise_for_status()\n\n            content_type = response.headers.get(\"Content-Type\", \"\")\n            if \"application/json\" not in content_type:\n                raise ValueError(\n                    f\"Expected JSON response from backend, got: {response.text}\"\n                )\n\n            response_data = response.json()\n            ai_response = response_data.get(\"response\")\n\n            if not isinstance(ai_response, str):\n                raise ValueError(\n                    \"Backend returned an unexpected response format.\"\n                )\n\n        except requests.exceptions.HTTPError as http_exc:\n            try:\n                error_data = response.json()\n                error_detail = error_data.get(\"detail\") or error_data.get(\"error\")\n            except ValueError:\n                error_detail = response.text or str(http_exc)\n\n            st.error(f\"Backend HTTP error {response.status_code}: {error_detail}\")\n            ai_response = None\n\n        except requests.exceptions.RequestException as req_exc:\n            st.error(f\"Request error: {req_exc}\")\n            ai_response = None\n\n        except ValueError as parse_exc:\n            st.error(f\"Response error: {parse_exc}\")\n            ai_response = None\n\n    if ai_response:\n\n        # Store AI Response\n        st.session_state.messages.append(\n            {\n                \"role\": \"assistant\",\n                \"content\": ai_response\n            }\n        )\n\n        with st.chat_message(\"assistant\"):\n            st.markdown(ai_response)\n",
    ),
]

for path, old, new in patches:
    text = path.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'pattern not found for {path}')
    path.write_text(text.replace(old, new), encoding='utf-8')
    print(f'patched {path}')
