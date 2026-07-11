from backend.database.db import get_connection


# GET ALL QUOTATIONS

def get_all_quotations():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT

            q.quotation_id,

            c.customer_name,

            q.vehicle_type,

            q.brand,

            q.model,

            q.policy_type,

            q.premium_amount,

            q.quotation_status,

            q.created_at

        FROM quotations q

        JOIN customers c

        ON q.customer_id = c.customer_id

        ORDER BY q.created_at DESC;
    """)

    columns = [col[0] for col in cursor.description]

    data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return data


# GET QUOTATION BY ID

def get_quotation_by_id(quotation_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT

            q.*,

            c.customer_name,
            c.email,
            c.phone

        FROM quotations q

        JOIN customers c

        ON q.customer_id = c.customer_id

        WHERE quotation_id=%s;
    """, (quotation_id,))

    row = cursor.fetchone()

    if row is None:
        cursor.close()
        conn.close()
        return None

    columns = [col[0] for col in cursor.description]

    result = dict(zip(columns, row))

    cursor.close()
    conn.close()

    return result


# SEARCH QUOTATIONS

def search_quotations(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT

            q.quotation_id,

            c.customer_name,

            q.vehicle_type,

            q.brand,

            q.model,

            q.policy_type,

            q.premium_amount,

            q.quotation_status,

            q.created_at

        FROM quotations q

        JOIN customers c

        ON q.customer_id = c.customer_id

        WHERE

            LOWER(c.customer_name) LIKE LOWER(%s)

            OR

            LOWER(q.brand) LIKE LOWER(%s)

            OR

            LOWER(q.model) LIKE LOWER(%s)

        ORDER BY q.created_at DESC;
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


# UPDATE QUOTATION STATUS

def update_quotation_status(quotation_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE quotations
        SET quotation_status=%s
        WHERE quotation_id=%s;
    """, (status, quotation_id))

    conn.commit()

    success = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return success


# DELETE QUOTATION

def delete_quotation(quotation_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM quotations
        WHERE quotation_id=%s;
    """, (quotation_id,))

    conn.commit()

    success = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return success

# CONVERT QUOTATION TO POLICY

def convert_to_policy(
    quotation_id,
    policy_number,
    start_date,
    expiry_date
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            customer_id,
            vehicle_type,
            policy_type,
            premium_amount
        FROM quotations
        WHERE quotation_id=%s;
    """, (quotation_id,))

    quotation = cursor.fetchone()

    if quotation is None:

        cursor.close()
        conn.close()

        return False

    customer_id, vehicle_type, policy_type, premium_amount = quotation

    cursor.execute("""
        INSERT INTO policies (

            quotation_id,
            customer_id,
            policy_number,
            vehicle_type,
            policy_type,
            premium_amount,
            start_date,
            expiry_date,
            policy_status

        )

        VALUES (

            %s,%s,%s,%s,%s,%s,%s,%s,'Active'

        );
    """, (

        quotation_id,
        customer_id,
        policy_number,
        vehicle_type,
        policy_type,
        premium_amount,
        start_date,
        expiry_date

    ))

    cursor.execute("""
        UPDATE quotations
        SET quotation_status='Bought'
        WHERE quotation_id=%s;
    """, (quotation_id,))

    conn.commit()

    success = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return success