import streamlit as st
import requests
import time

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Personal Agentic AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# PREMIUM CSS
# =========================================

st.markdown("""
<style>

/* =========================================
REMOVE STREAMLIT DEFAULT SPACE
========================================= */

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* =========================================
MAIN APP BACKGROUND
========================================= */

.stApp {

    background:
        radial-gradient(circle at top right,
        rgba(37,99,235,0.20),
        transparent 25%),

        radial-gradient(circle at bottom left,
        rgba(59,130,246,0.12),
        transparent 20%),

        linear-gradient(
            135deg,
            #020617 0%,
            #030712 25%,
            #050816 55%,
            #000000 100%
        );

    color: white;
}

/* =========================================
HIDE STREAMLIT MENU
========================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* =========================================
SIDEBAR
========================================= */

[data-testid="stSidebar"] {

    background: rgba(5,10,20,0.92);

    border-right: 1px solid rgba(255,255,255,0.06);

    backdrop-filter: blur(20px);

    padding-top: 20px;
}

/* =========================================
SIDEBAR TEXT
========================================= */

[data-testid="stSidebar"] * {
    color: #E5E7EB !important;
}

/* =========================================
TITLE
========================================= */

.main-title {

    text-align: center;

    font-size: 64px;

    font-weight: 800;

    margin-top: 10px;

    background: linear-gradient(
        to right,
        #FFFFFF,
        #93C5FD,
        #3B82F6
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    line-height: 1.1;
}

.sub-title {

    text-align: center;

    color: #CBD5E1;

    font-size: 20px;

    margin-top: 10px;

    margin-bottom: 40px;
}

/* =========================================
USER CHAT
========================================= */

.chat-user {

    background: linear-gradient(
        135deg,
        #2563EB,
        #1D4ED8
    );

    padding: 22px;

    border-radius: 24px;

    margin-bottom: 20px;

    color: white;

    font-size: 17px;

    line-height: 1.8;

    box-shadow:
        0 0 30px rgba(37,99,235,0.35);

    animation: fadeIn 0.4s ease;
}

/* =========================================
AI CHAT
========================================= */

.chat-ai {

    background: rgba(15,23,42,0.82);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 24px;

    border-radius: 24px;

    margin-bottom: 22px;

    color: #F3F4F6;

    font-size: 17px;

    line-height: 1.8;

    backdrop-filter: blur(18px);

    box-shadow:
        0 0 25px rgba(59,130,246,0.10);

    animation: fadeIn 0.4s ease;
}

/* =========================================
CHAT INPUT FIX
========================================= */

.stChatInputContainer {

    background: rgba(15,23,42,0.95) !important;

    border-radius: 24px !important;

    border: 1px solid rgba(255,255,255,0.08) !important;

    padding: 12px !important;

    backdrop-filter: blur(20px);

    box-shadow:
        0 0 20px rgba(37,99,235,0.20);

    margin-top: 10px;
}

/* =========================================
CHAT INPUT TEXT FIX
========================================= */

.stChatInputContainer textarea {

    color: white !important;

    background: transparent !important;

    font-size: 16px !important;
}

/* =========================================
TEXT AREA
========================================= */

textarea {

    background: rgba(15,23,42,0.90) !important;

    color: white !important;

    border-radius: 16px !important;

    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* =========================================
SELECT BOX
========================================= */

div[data-baseweb="select"] > div {

    background: rgba(15,23,42,0.85) !important;

    color: white !important;

    border-radius: 14px !important;

    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* =========================================
BUTTONS
========================================= */

.stButton > button {

    background: linear-gradient(
        135deg,
        #2563EB,
        #1D4ED8
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 12px 24px;

    font-weight: 700;

    transition: 0.3s ease;

    box-shadow:
        0 0 20px rgba(37,99,235,0.30);
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 0 35px rgba(37,99,235,0.50);
}

/* =========================================
ANIMATION
========================================= */

@keyframes fadeIn {

    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* =========================================
SCROLLBAR
========================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {

    background: #2563EB;

    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HERO SECTION
# =========================================

st.markdown(
    """
    <div class="main-title">
        Where Ideas Take Flight
    </div>

    <div class="sub-title">
        Ask, explore, and co-create with your intelligent AI assistant
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.markdown("## ⚙️ AI Settings")

    provider = st.selectbox(
        "Model Provider",
        ["groq", "openai"]
    )

    if provider == "groq":

        model = st.selectbox(
            "Choose Model",
            [
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile"
            ]
        )

    else:

        model = st.selectbox(
            "Choose Model",
            [
                "gpt-4o-mini"
            ]
        )

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a professional AI assistant.",
        height=150
    )

    st.divider()

    st.markdown("### 🚀 Features")

    st.markdown("""
    ✅ Multi-LLM Support  
    ✅ LangGraph AI Agent  
    ✅ FastAPI Backend  
    ✅ Streaming Responses  
    ✅ Modern SaaS UI  
    """)

    st.divider()

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []
        st.rerun()

# =========================================
# SESSION STATE
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================
# DISPLAY CHAT HISTORY
# =========================================

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f"""
            <div class="chat-user">
            👤 <b>You</b><br><br>
            {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="chat-ai">
            🤖 <b>AI Assistant</b><br><br>
            {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================
# CHAT INPUT
# =========================================

user_input = st.chat_input(
    "Ask anything..."
)

# =========================================
# HANDLE CHAT
# =========================================

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    st.markdown(
        f"""
        <div class="chat-user">
        👤 <b>You</b><br><br>
        {user_input}
        </div>
        """,
        unsafe_allow_html=True
    )

    API_URL = "http://127.0.0.1:8000/chat"

    payload = {
        "message": user_input,
        "provider": provider,
        "model": model,
        "system_prompt": system_prompt,
    }

    with st.spinner("🤖 AI is thinking..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=120
            )

            if response.status_code == 200:

                ai_response = response.json()["response"]

            else:

                ai_response = f"Backend Error: {response.text}"

        except Exception as e:

            ai_response = f"Request Error: {str(e)}"

    message_placeholder = st.empty()

    full_response = ""

    for chunk in ai_response.split():

        full_response += chunk + " "

        message_placeholder.markdown(
            f"""
            <div class="chat-ai">
            🤖 <b>AI Assistant</b><br><br>
            {full_response}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.02)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )