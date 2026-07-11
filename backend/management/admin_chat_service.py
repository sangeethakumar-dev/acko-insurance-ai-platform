import re

from backend.database.admin_chat_queries import (
    execute_sql_query,
    save_admin_chat,
    get_chat_history,
    clear_chat_history
)

from backend.utils.gemini_client import generate_content


# ==========================
# GENERATE SQL
# ==========================

def generate_sql(question: str):

    prompt = f"""
You are an expert PostgreSQL assistant.

Convert the user's question into ONLY ONE PostgreSQL SELECT query.

Database Schema

customers
---------
customer_id
customer_name
email
phone
address
created_at

quotations
----------
quotation_id
customer_id
vehicle_type
brand
model
policy_type
premium_amount
quotation_status
created_at

policies
--------
policy_id
quotation_id
customer_id
policy_number
vehicle_type
policy_type
premium_amount
start_date
expiry_date
policy_status
created_at

claims
------
claim_id
claim_number
customer_name
vehicle_type
brand
model
policy_type
claim_status
fraud_risk
recommended_payout
pdf_path
created_at

claim_images
------------
image_id
claim_id
image_path
uploaded_at

claim_reports
-------------
report_id
claim_id
report
created_at

admin_chat_logs
---------------
chat_id
admin_question
ai_answer
created_at

Important Rules

1. Return ONLY SQL.
2. Return ONLY one SELECT query.
3. Never explain.
4. Never use markdown.
5. Never use ```sql.
6. Never generate DELETE.
7. Never generate UPDATE.
8. Never generate INSERT.
9. Never generate DROP.
10. Never generate ALTER.
11. Never use columns that are not listed above.
12. The claims table DOES NOT contain customer_id.
13. The claims table DOES NOT contain policy_id.
14. Use claim_status instead of status.
15. Use quotation_status instead of status.
16. Use policy_status instead of status.
17. If customer information is requested from claims, use customer_name.
18. If the question asks for pending claims, use:

SELECT COUNT(*) FROM claims
WHERE claim_status='Pending';

Question:

VERY IMPORTANT

The database NEVER contains a column named "status".

Never generate:

status

Always use the correct column:

claims -> claim_status
quotations -> quotation_status
policies -> policy_status

If you generate the column "status", your answer is WRONG.

{question}
"""

    sql = generate_content(prompt).strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    # Fix common column mistakes
    sql = re.sub(r"\bstatus\b", "claim_status", sql, flags=re.IGNORECASE)

    return sql


# VALIDATE SQL

def validate_sql(sql):

    sql = sql.strip()

    if not sql.upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")
    
    if re.search(r"\bstatus\b", sql, re.IGNORECASE):
        raise ValueError(
        "Generated SQL uses 'status'. Use claim_status, quotation_status or policy_status."
            )

    blocked = [
        "DELETE",
        "UPDATE",
        "DROP",
        "ALTER",
        "INSERT",
        "TRUNCATE",
        "CREATE"
    ]

    upper = sql.upper()

    for keyword in blocked:
        if keyword in upper:
            raise ValueError("Unsafe SQL generated.")

    return True


# ==========================
# SUMMARIZE RESULT
# ==========================

def summarize_result(question, result):

    prompt = f"""
You are an Insurance Management AI Assistant.

Question:
{question}

SQL Result:
{result}

Give a short professional answer for the admin.

Do not mention SQL.

Keep it concise.
"""

    return generate_content(prompt)


# ADMIN CHAT

def admin_chat(question):

    sql = generate_sql(question)

    validate_sql(sql)

    result = execute_sql_query(sql)

    answer = summarize_result(question, result)

    save_admin_chat(
        question,
        answer
    )

    return {
        "question": question,
        "generated_sql": sql,
        "result": result,
        "answer": answer
    }


# CHAT HISTORY

def get_admin_chat_history():

    return get_chat_history()


# CLEAR HISTORY

def clear_admin_history():

    clear_chat_history()

    return {
        "message": "Chat history cleared."
    }