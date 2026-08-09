import os

from groq import Groq
from langchain.tools import tool
from tavily import TavilyClient


# ============================================================
# CLIENTS
# ============================================================

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# ============================================================
# WEB SEARCH TOOL
# ============================================================

@tool
def web_search(query: str) -> str:
    """
    Search the web using Tavily and summarize
    the results using Groq.
    """

    # --------------------------------------------------------
    # Tavily Search
    # --------------------------------------------------------

    results = tavily_client.search(
        query=query,
        search_depth="basic",
        max_results=5
    )

    if not results.get("results"):
        return "No relevant search results found."


    # --------------------------------------------------------
    # Prepare Search Results
    # --------------------------------------------------------

    search_text = "\n\n".join(
        [
            f"Title: {result['title']}\n"
            f"URL: {result['url']}\n"
            f"Content: {result['content']}"
            for result in results["results"]
        ]
    )


    # --------------------------------------------------------
    # Groq Prompt
    # --------------------------------------------------------

    prompt = f"""
You are a helpful AI web search assistant.

Answer the user's question using ONLY the
search results provided below.

If the information is not available in the
search results, say that it could not be found.

User Question:
{query}

Search Results:
{search_text}
"""


    # --------------------------------------------------------
    # Groq Summary
    # --------------------------------------------------------

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )


    return response.choices[0].message.content