from backend.database.db import get_connection


# ==========================================
# CUSTOMER REGISTER
# ==========================================

def register_customer(
    customer_name,
    email,
    password,
    phone,
    address
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO customers
        (
            customer_name,
            email,
            password,
            phone,
            address
        )

        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )

        RETURNING customer_id;
        """,
        (
            customer_name,
            email,
            password,
            phone,
            address
        )
    )

    customer_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return customer_id


# ==========================================
# CUSTOMER LOGIN
# ==========================================

def customer_login(
    email,
    password
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            customer_id,
            customer_name,
            email

        FROM customers

        WHERE
            email = %s
            AND password = %s;
        """,
        (
            email,
            password
        )
    )

    customer = cursor.fetchone()

    cursor.close()
    conn.close()

    return customer


# ==========================================
# ADMIN LOGIN
# ==========================================

def admin_login(
    email,
    password
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            admin_id,
            admin_name,
            email

        FROM admins

        WHERE
            email = %s
            AND password = %s;
        """,
        (
            email,
            password
        )
    )

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    return admin


# ==========================================
# CHECK CUSTOMER EMAIL
# ==========================================

def customer_email_exists(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT customer_id

        FROM customers

        WHERE email = %s;
        """,
        (email,)
    )

    exists = cursor.fetchone()

    cursor.close()
    conn.close()

    return exists


# ==========================================
# CHECK ADMIN EMAIL
# ==========================================

def admin_email_exists(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT admin_id

        FROM admins

        WHERE email = %s;
        """,
        (email,)
    )

    exists = cursor.fetchone()

    cursor.close()
    conn.close()

    return exists