
from collaboration import collaborate

from collaboration import collaborate
from agents.math_agent import math_agent
from agents.pdf_agent import pdf_agent
from agents.sql_agent import sql_agent
from agents.web_agent import web_agent
from agents.weather_agent import weather_agent
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=0
)
SYSTEM_PROMPT = """
You are a Supervisor Agent.

Your job is to select the SINGLE best agent to answer the user's question.

Available Agents:

1. math
Use for:
- arithmetic
- mathematics
- percentages
- calculations
- equations

2. pdf
Use for:
- questions about uploaded PDFs
- summarize PDF
- explain PDF
- retrieve information from PDF

3. sql
Use for:
- employee database
- salary
- attendance
- leaves
- projects
- performance
- attrition
- MySQL
- HR database

4. weather
Use for:
- weather
- temperature
- forecast
- humidity
- rain

5. collaboration
Use ONLY when the question requires BOTH the uploaded PDF and the HR database.

Examples:
- Compare employees in the PDF with the database.
- Verify whether employees in the PDF exist in the database.
- Compare salaries in the PDF with the HR database.
- Generate a report using PDF and database information.
- Find mismatches between the PDF and the employee database.
- Reconcile employee records from the PDF with MySQL.

6. web
Use for:
- general knowledge
- internet search
- current events
- questions not covered by the other agents

Return ONLY one of these words:

math
pdf
sql
weather
collaboration
web

Do not provide explanations.
Return exactly one word.
"""

def supervisor(question):

    response = llm.invoke(
        SYSTEM_PROMPT + "\n\nQuestion:\n" + question
    )

    route = response.content.lower().strip()

    print("Supervisor Selected:", route)

    if route == "math":
        return math_agent

    elif route == "pdf":
        return pdf_agent

    elif route == "sql":
        return sql_agent

    elif route == "weather":
        return weather_agent

    elif route == "collaboration":
        return collaborate

    else:
        return web_agent