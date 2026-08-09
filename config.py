import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# API KEYS
# ==========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# ==========================
# Groq Model
# ==========================

MODEL_NAME = "openai/gpt-oss-120b"

# Alternative models:
# MODEL_NAME = "llama-3.3-70b-versatile"
# MODEL_NAME = "llama-3.1-8b-instant"


# ==========================
# MySQL
# ==========================

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


# ==========================
# Embedding Model
# ==========================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ==========================
# Paths
# ==========================

UPLOAD_FOLDER = "uploads"
CHROMA_DB = "chroma_db"


# ==========================
# Retrieval
# ==========================

TOP_K = 3