from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver



from tools.pdf_tool import pdf_tool

# ==========================
# LLM
# ==========================
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

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
# PDF Agent
# ==========================

pdf_agent = create_react_agent(
    model=llm,
    tools=[pdf_tool],
    checkpointer=memory
)