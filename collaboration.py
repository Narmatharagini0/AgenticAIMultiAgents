from agents.pdf_agent import pdf_agent
from agents.sql_agent import sql_agent
from agents.report_agent import report_agent


def collaborate(question, config):

    # ==========================
    # Step 1 : PDF Agent
    # ==========================
    print("========== STEP 1 : PDF AGENT ==========")

    pdf_prompt = f"""
You are a PDF extraction agent.

User Question:
{question}

Your task:
- Read ONLY the uploaded PDF.
- Extract all employee details relevant to the user's question.
- Do NOT answer the question.
- Do NOT mention databases.
- Return only the extracted employee information.
"""

    pdf_response = pdf_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": pdf_prompt
                }
            ]
        },
        config=config
    )

    pdf_answer = pdf_response["messages"][-1].content

    print(pdf_answer)

    # ==========================
    # Step 2 : SQL Agent
    # ==========================
    print("========== STEP 2 : SQL AGENT ==========")

    sql_prompt = f"""
You are an HR database assistant.

The following employee information was extracted from a PDF.

{pdf_answer}

Original User Question:
{question}

Use ONLY the extracted employee information to query the MySQL employee table.

Do NOT say you cannot access PDFs.
Assume the above employee information is correct.
Return only the database results.
"""

    sql_response = sql_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": sql_prompt
                }
            ]
        },
        config=config
    )

    sql_answer = sql_response["messages"][-1].content

    print(sql_answer)

    # ==========================
    # Step 3 : Report Agent
    # ==========================
    print("========== STEP 3 : REPORT AGENT ==========")

    report_prompt = f"""
Original User Question:
{question}

PDF Employee Data:
{pdf_answer}

Database Result:
{sql_answer}

Generate a comparison report containing:

1. Employees present in both PDF and database.
2. Employees missing in the database.
3. Employees missing in the PDF.
4. Any differences found.
"""

    report_response = report_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": report_prompt
                }
            ]
        },
        config=config
    )

    return report_response