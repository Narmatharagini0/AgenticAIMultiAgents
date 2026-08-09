from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from tools.weather_tool import weather
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

# llm = ChatGoogleGenerativeAI(
#     model=MODEL_NAME,
#     api_key=GEMINI_API_KEY,
#     temperature=0
# )

# ==========================
# Memory
# ==========================

memory = MemorySaver()

# ==========================
# Weather Agent
# ==========================

weather_agent = create_react_agent(
    model=llm,
    tools=[weather],
    checkpointer=memory
)