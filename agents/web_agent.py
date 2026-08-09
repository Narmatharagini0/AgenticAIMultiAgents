from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME
from tools.web_tool import web_search

# ==========================
# LLM
# ==========================

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=0
)

# ==========================
# Memory
# ==========================

memory = MemorySaver()

# ==========================
# Web Agent
# ==========================

web_agent = create_react_agent(
    model=llm,
    tools=[web_search],
    checkpointer=memory
)