from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from tools.sql_tool import sql_agent
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=0
)
# ==========================
# LLM
# ==========================



# ==========================
# Memory
# ==========================

memory = MemorySaver()

# ==========================
# SQL Agent
# ==========================

sql_agent = create_react_agent(
    model=llm,
    tools=[sql_agent],
    checkpointer=memory
)