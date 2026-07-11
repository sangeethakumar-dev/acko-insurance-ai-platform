from backend.database.db import get_connection


# EXECUTE SQL QUERY

def execute_sql_query(sql_query: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(sql_query)

        # No data returned
        if cursor.description is None:

            conn.commit()

            cursor.close()
            conn.close()

            return []

        columns = [column[0] for column in cursor.description]

        rows = cursor.fetchall()

        result = [

            dict(zip(columns, row))

            for row in rows

        ]

        cursor.close()
        conn.close()

        return result

    except Exception as e:

        cursor.close()
        conn.close()

        raise e


# SAVE ADMIN CHAT

def save_admin_chat(question, answer):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO admin_chat_logs(

            admin_question,

            ai_answer

        )

        VALUES(%s,%s);

    """, (

        question,

        answer

    ))

    conn.commit()

    cursor.close()
    conn.close()


# GET CHAT HISTORY

def get_chat_history(limit=20):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            chat_id,

            admin_question,

            ai_answer,

            created_at

        FROM admin_chat_logs

        ORDER BY created_at DESC

        LIMIT %s;

    """, (limit,))

    columns = [col[0] for col in cursor.description]

    result = [

        dict(zip(columns, row))

        for row in cursor.fetchall()

    ]

    cursor.close()
    conn.close()

    return result


# CLEAR CHAT HISTORY

def clear_chat_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        DELETE FROM admin_chat_logs;

    """)

    conn.commit()

    cursor.close()
    conn.close()

    return True