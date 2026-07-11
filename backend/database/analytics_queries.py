from backend.database.db import get_connection


# MONTHLY REVENUE

def get_monthly_revenue():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            TO_CHAR(created_at,'Mon') AS month,

            COALESCE(SUM(premium_amount),0) AS revenue

        FROM policies

        GROUP BY month,
                 DATE_TRUNC('month',created_at)

        ORDER BY DATE_TRUNC('month',created_at);

    """)

    columns=[col[0] for col in cursor.description]

    result=[
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return result


# CLAIM STATUS ANALYTICS

def get_claim_status_analytics():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        SELECT

            claim_status,

            COUNT(*)

        FROM claims

        GROUP BY claim_status;

    """)

    result=dict(cursor.fetchall())

    cursor.close()
    conn.close()

    return result


# FRAUD ANALYTICS

def get_fraud_analytics():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        SELECT

            fraud_risk,

            COUNT(*)

        FROM claims

        GROUP BY fraud_risk;

    """)

    result=dict(cursor.fetchall())

    cursor.close()
    conn.close()

    return result


# POLICY ANALYTICS

def get_policy_analytics():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        SELECT

            policy_status,

            COUNT(*)

        FROM policies

        GROUP BY policy_status;

    """)

    result=dict(cursor.fetchall())

    cursor.close()
    conn.close()

    return result


# VEHICLE TYPE ANALYTICS

def get_vehicle_analytics():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        SELECT

            vehicle_type,

            COUNT(*)

        FROM policies

        GROUP BY vehicle_type;

    """)

    result=dict(cursor.fetchall())

    cursor.close()
    conn.close()

    return result


# POLICY TYPE ANALYTICS

def get_policy_type_analytics():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        SELECT

            policy_type,

            COUNT(*)

        FROM policies

        GROUP BY policy_type;

    """)

    result=dict(cursor.fetchall())

    cursor.close()
    conn.close()

    return result


# CLAIM PAYOUT ANALYTICS

def get_claim_payout_analytics():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        SELECT

            COALESCE(SUM(recommended_payout),0)

        FROM claims;

    """)

    payout=cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {

        "total_claim_payout": float(payout)

    }


# CUSTOMER ANALYTICS

def get_customer_analytics():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM customers;

    """)

    total=cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {

        "total_customers": total

    }


# OVERALL ANALYTICS

def get_overall_analytics():

    return {

        "monthly_revenue": get_monthly_revenue(),

        "claim_status": get_claim_status_analytics(),

        "fraud": get_fraud_analytics(),

        "policy_status": get_policy_analytics(),

        "vehicle_type": get_vehicle_analytics(),

        "policy_type": get_policy_type_analytics(),

        "claim_payout": get_claim_payout_analytics(),

        "customers": get_customer_analytics()

    }