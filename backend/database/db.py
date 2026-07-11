import psycopg2

from backend.utils.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def get_connection():
    """
    Create PostgreSQL connection.
    """

    try:

        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        return connection

    except Exception as e:

        print(f"Database Connection Error : {e}")

        raise e
    

if __name__ == "__main__":

    conn = get_connection()

    print("Connected Successfully!")

    conn.close()

    print("Connection Closed!")