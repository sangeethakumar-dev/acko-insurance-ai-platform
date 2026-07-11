from backend.database.db import get_connection


# GET ALL CUSTOMERS

def get_all_customers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            customer_id,

            customer_name,

            email,

            phone,

            address,

            created_at

        FROM customers

        ORDER BY customer_name;

    """)

    columns = [col[0] for col in cursor.description]

    customers = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return customers


# GET CUSTOMER BY ID

def get_customer_by_id(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM customers

        WHERE customer_id=%s;

    """, (customer_id,))

    row = cursor.fetchone()

    if row is None:
        cursor.close()
        conn.close()
        return None

    columns = [col[0] for col in cursor.description]

    customer = dict(zip(columns, row))

    cursor.close()
    conn.close()

    return customer


# SEARCH CUSTOMERS

def search_customers(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            customer_id,

            customer_name,

            email,

            phone,

            address,

            created_at

        FROM customers

        WHERE

            LOWER(customer_name) LIKE LOWER(%s)

            OR

            LOWER(email) LIKE LOWER(%s)

            OR

            LOWER(phone) LIKE LOWER(%s)

        ORDER BY customer_name;

    """, (

        f"%{keyword}%",

        f"%{keyword}%",

        f"%{keyword}%"

    ))

    columns = [col[0] for col in cursor.description]

    result = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return result


# CUSTOMER POLICIES

def get_customer_policies(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            policy_number,

            vehicle_type,

            policy_type,

            premium_amount,

            start_date,

            expiry_date,

            policy_status

        FROM policies

        WHERE customer_id=%s

        ORDER BY created_at DESC;

    """, (customer_id,))

    columns = [col[0] for col in cursor.description]

    policies = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return policies


# CUSTOMER CLAIMS

def get_customer_claims(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    # Get customer name first
    cursor.execute("""
        SELECT customer_name
        FROM customers
        WHERE customer_id=%s;
    """, (customer_id,))

    row = cursor.fetchone()

    if row is None:

        cursor.close()
        conn.close()

        return []

    customer_name = row[0]

    # Fetch claims using customer_name
    cursor.execute("""

        SELECT

            claim_number,

            vehicle_type,

            claim_status,

            fraud_risk,

            recommended_payout,

            created_at

        FROM claims

        WHERE customer_name=%s

        ORDER BY created_at DESC;

    """, (customer_name,))

    columns = [col[0] for col in cursor.description]

    claims = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return claims


# CUSTOMER STATISTICS

def get_customer_statistics(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    # Total Policies

    cursor.execute("""

        SELECT COUNT(*)

        FROM policies

        WHERE customer_id=%s;

    """, (customer_id,))

    total_policies = cursor.fetchone()[0]

    # Total Claims

    cursor.execute("""

    SELECT customer_name

    FROM customers

    WHERE customer_id=%s;

""", (customer_id,))

    row = cursor.fetchone()

    if row is None:

        total_claims = 0

    else:

        customer_name = row[0]

    cursor.execute("""

        SELECT COUNT(*)

        FROM claims

        WHERE customer_name=%s;

    """, (customer_name,))

    total_claims = cursor.fetchone()[0]

    # Total Premium Paid

    cursor.execute("""

        SELECT COALESCE(SUM(premium_amount),0)

        FROM policies

        WHERE customer_id=%s;

    """, (customer_id,))

    premium_paid = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {

        "total_policies": total_policies,

        "total_claims": total_claims,

        "premium_paid": float(premium_paid)

    }


# DELETE CUSTOMER

def delete_customer(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        DELETE FROM customers

        WHERE customer_id=%s;

    """, (customer_id,))

    conn.commit()

    success = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return success