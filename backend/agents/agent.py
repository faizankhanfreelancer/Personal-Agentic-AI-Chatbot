from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent

from backend.config.settings import (
    OPENAI_API_KEY,
    GROQ_API_KEY,
)

# Search Tool
# search_tool = TavilySearchResults(max_results=2)


# Dynamic LLM Loader
def get_llm(provider, model):

    if provider == "openai":

        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is missing. Please set it in .env.")

        return ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model=model,
            temperature=0.7,
        )

    elif provider == "groq":

        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing. Please set it in .env.")

        return ChatGroq(
            api_key=GROQ_API_KEY,
            model=model,
            temperature=0.7,
        )

    else:
        raise ValueError("Invalid provider")


# Main Agent Function
def run_agent(message, provider, model, system_prompt):

    llm = get_llm(provider, model)

    tools = []

    agent = create_react_agent(
        llm,
        tools,
    )

    response = agent.invoke(
        {
            "messages": [
                ("system", system_prompt),
                ("human", message),
            ]
        }
    )

    final_response = response["messages"][-1].content

    return final_response