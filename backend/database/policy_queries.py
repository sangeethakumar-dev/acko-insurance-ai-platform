from backend.database.db import get_connection


# ==========================================================
# GET ALL POLICIES
# ==========================================================

def get_all_policies():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.policy_id,
            p.policy_number,
            c.customer_name,
            p.vehicle_type,
            p.policy_type,
            p.premium_amount,
            p.start_date,
            p.expiry_date,
            p.policy_status,
            p.created_at

        FROM policies p

        JOIN customers c
        ON p.customer_id = c.customer_id

        ORDER BY p.created_at DESC;
    """)

    columns = [col[0] for col in cursor.description]

    result = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return result


# ==========================================================
# GET POLICY BY ID
# ==========================================================

def get_policy_by_id(policy_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.*,
            c.customer_name,
            c.email,
            c.phone,
            c.address

        FROM policies p

        JOIN customers c
        ON p.customer_id = c.customer_id

        WHERE p.policy_id = %s;
    """, (policy_id,))

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


# ==========================================================
# SEARCH POLICIES
# ==========================================================

def search_policies(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.policy_id,
            p.policy_number,
            c.customer_name,
            p.vehicle_type,
            p.policy_type,
            p.premium_amount,
            p.policy_status,
            p.expiry_date

        FROM policies p

        JOIN customers c
        ON p.customer_id = c.customer_id

        WHERE

            LOWER(c.customer_name) LIKE LOWER(%s)

            OR LOWER(p.policy_number) LIKE LOWER(%s)

            OR LOWER(p.vehicle_type) LIKE LOWER(%s)

        ORDER BY p.created_at DESC;
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


# ==========================================================
# UPDATE POLICY STATUS
# ==========================================================

def update_policy_status(policy_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE policies
        SET policy_status=%s
        WHERE policy_id=%s;
    """, (status, policy_id))

    conn.commit()

    success = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return success


# ==========================================================
# RENEW POLICY
# ==========================================================

def renew_policy(policy_id, start_date, expiry_date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE policies

        SET
            start_date=%s,
            expiry_date=%s,
            policy_status='Active'

        WHERE policy_id=%s;
    """, (
        start_date,
        expiry_date,
        policy_id
    ))

    conn.commit()

    success = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return success


# ==========================================================
# DELETE POLICY
# ==========================================================

def delete_policy(policy_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM policies
        WHERE policy_id=%s;
    """, (policy_id,))

    conn.commit()

    success = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return success


# ==========================================================
# EXPIRING POLICIES
# ==========================================================

def get_expiring_policies(days=30):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.policy_number,
            c.customer_name,
            p.expiry_date,
            p.policy_status

        FROM policies p

        JOIN customers c
        ON p.customer_id = c.customer_id

        WHERE
            p.expiry_date <= CURRENT_DATE + (%s * INTERVAL '1 day')

        ORDER BY p.expiry_date;
    """, (days,))

    columns = [col[0] for col in cursor.description]

    result = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return result