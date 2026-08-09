from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME
from tools.calculator_tool import calculator


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
# Math Agent
# ==========================

math_agent = create_react_agent(
    model=llm,
    tools=[calculator],
    checkpointer=memory
)