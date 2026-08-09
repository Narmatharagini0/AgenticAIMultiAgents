# 🤖 Multi-Agent AI Assistant

A Generative AI based **Multi-Agent Assistant** built using Python, LangGraph, Groq, RAG, ChromaDB, MySQL, Tavily, Weather API and Streamlit.

The application uses a **Supervisor Agent** to understand the user's query and route it to the appropriate specialized AI agent.

## 🚀 Features

- Multi-Agent architecture using LangGraph
- Supervisor Agent for intelligent agent routing
- Groq LLM for fast AI responses
- RAG-based PDF question answering
- MySQL database interaction
- Web search using Tavily
- Real-time weather information using WeatherAPI
- Mathematical calculations
- Report and employee data analysis
- ChromaDB vector database
- HuggingFace sentence-transformer embeddings
- Streamlit user interface
- Environment variables for API keys and credentials

## 🧠 Agents

### Supervisor Agent

Analyzes the user's question and selects the appropriate specialist agent.

### Math Agent

Handles mathematical calculations.

Example:

    Calculate 125 * 45

### SQL Agent

Handles database-related questions and interacts with MySQL.

Example:

    Show employees from the IT department.

### Web Agent

Uses Tavily to search the web and Groq to summarize the retrieved information.

Example:

    What are the latest developments in Generative AI?

### Weather Agent

Uses WeatherAPI to retrieve current weather information.

Example:

    What is the current weather in Chennai?

### PDF Agent

Uses Retrieval-Augmented Generation (RAG) to answer questions from PDF documents.

Example:

    Who is the best performing employee?

### Report Agent

Handles report-related analysis and retrieves relevant information from available data sources.

## 📄 RAG Pipeline

The PDF question-answering system uses the following process:

1. PDF document is loaded using PyPDF.
2. Extracted text is split into smaller chunks.
3. HuggingFace embeddings are generated for the chunks.
4. Embeddings are stored in ChromaDB.
5. User questions are converted into embeddings.
6. Relevant document chunks are retrieved.
7. Retrieved information is provided to the Groq LLM.
8. The LLM generates the final answer based on the retrieved context.

Embedding model:

    sentence-transformers/all-MiniLM-L6-v2

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| LangGraph | Multi-agent orchestration |
| LangChain | LLM and tool integration |
| Groq | Large Language Model |
| ChromaDB | Vector database |
| HuggingFace | Text embeddings |
| Tavily | Web search |
| WeatherAPI | Weather information |
| MySQL | Database |
| PyPDF | PDF processing |
| Streamlit | Web interface |
| python-dotenv | Environment configuration |

## 📁 Project Structure

    agent_ai_project_WorkingGROQ/
    │
    ├── agents/
    │   ├── math_agent.py
    │   ├── pdf_agent.py
    │   ├── report_agent.py
    │   ├── sql_agent.py
    │   ├── weather_agent.py
    │   ├── web_agent.py
    │   └── __init__.py
    │
    ├── tools/
    │   ├── math_tool.py
    │   ├── pdf_tool.py
    │   ├── report_tool.py
    │   ├── sql_tool.py
    │   ├── weather_tool.py
    │   └── web_tool.py
    │
    ├── rag/
    │   ├── rag_service.py
    │   ├── retriever.py
    │   └── vector_store.py
    │
    ├── data/
    │
    ├── pdfs/
    │
    ├── uploads/
    │
    ├── app.py
    ├── config.py
    ├── supervisor.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## ⚙️ Installation

### 1. Clone the repository

    git clone YOUR_GITHUB_REPOSITORY_URL

Navigate into the project:

    cd agent_ai_project_WorkingGROQ

### 2. Create a virtual environment

    python -m venv .venv

Activate the environment on Windows PowerShell:

    .venv\Scripts\Activate.ps1

### 3. Install dependencies

    python -m pip install -r requirements.txt

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

    GROQ_API_KEY=your_groq_api_key
    TAVILY_API_KEY=your_tavily_api_key
    WEATHER_API_KEY=your_weather_api_key

    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    MYSQL_USER=your_mysql_user
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_DATABASE=your_database

### Security

Never upload your `.env` file to GitHub.

Add these to `.gitignore`:

    .env
    .venv/
    __pycache__/
    chroma_db/

## ▶️ Run the Application

Start the Streamlit application:

    streamlit run app.py

The application will open in your browser.

## 💡 Example Queries

### Weather

    What is the current weather in Chennai?

### Web Search

    What are the latest developments in Generative AI?

### PDF / RAG

    Who is the best performing employee?

### SQL

    Show employees from the IT department.

### Mathematics

    Calculate 1250 * 35

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Generative AI
- Agentic AI
- Multi-Agent Systems
- LangGraph
- LangChain
- Tool Calling
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embeddings
- LLM integration
- API integration
- Database integration
- Streamlit application development

## 🚀 Future Enhancements

- Add more specialized agents
- Improve supervisor routing
- Add conversation memory
- Support multiple PDF uploads
- Add document-level citations
- Improve SQL generation and validation
- Add automated testing for agents and tools
- Deploy the application to the cloud

## 👩‍💻 Author

Built as a practical Generative AI and Agentic AI project to explore multi-agent architecture, RAG, LLM integration, API integration, database interaction and AI-powered applications.

---

**Powered by LangGraph • Groq • ChromaDB • MySQL • Tavily • Streamlit • Multi-Agent AI**