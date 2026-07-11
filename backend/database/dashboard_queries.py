from backend.database.db import get_connection

# DASHBOARD SUMMARY CARDS

def get_dashboard_summary_data():

    conn = get_connection()
    cursor = conn.cursor()

    # Total Customers
    cursor.execute("SELECT COUNT(*) FROM customers;")
    total_customers = cursor.fetchone()[0]

    # Total Quotations
    cursor.execute("SELECT COUNT(*) FROM quotations;")
    total_quotations = cursor.fetchone()[0]

    # Total Policies
    cursor.execute("SELECT COUNT(*) FROM policies;")
    total_policies = cursor.fetchone()[0]

    # Total Claims
    cursor.execute("SELECT COUNT(*) FROM claims;")
    total_claims = cursor.fetchone()[0]

    # High Fraud Claims
    cursor.execute("""
        SELECT COUNT(*)
        FROM claims
        WHERE fraud_risk='High';
    """)
    fraud_alerts = cursor.fetchone()[0]

    # Total Premium Revenue
    cursor.execute("""
        SELECT COALESCE(SUM(premium_amount),0)
        FROM policies;
    """)
    premium_revenue = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        "customers": total_customers,
        "quotations": total_quotations,
        "policies": total_policies,
        "claims": total_claims,
        "fraud_alerts": fraud_alerts,
        "premium_revenue": float(premium_revenue)
    }


# CHART DATA

def get_dashboard_chart_data():

    conn = get_connection()
    cursor = conn.cursor()

    # Quotation Status
    
    cursor.execute("""
        SELECT quotation_status, COUNT(*)
        FROM quotations
        GROUP BY quotation_status;
    """)

    quotation_chart = dict(cursor.fetchall())

    
    # Policy Status
    
    cursor.execute("""
        SELECT policy_status, COUNT(*)
        FROM policies
        GROUP BY policy_status;
    """)

    policy_chart = dict(cursor.fetchall())

    
    # Claim Status
    
    cursor.execute("""
        SELECT claim_status, COUNT(*)
        FROM claims
        GROUP BY claim_status;
    """)

    claim_chart = dict(cursor.fetchall())

    
    # Fraud Distribution
    
    cursor.execute("""
        SELECT fraud_risk, COUNT(*)
        FROM claims
        GROUP BY fraud_risk;
    """)

    fraud_chart = dict(cursor.fetchall())

    
    # Vehicle Type Distribution
    
    cursor.execute("""
        SELECT vehicle_type, COUNT(*)
        FROM policies
        GROUP BY vehicle_type;
    """)

    vehicle_chart = dict(cursor.fetchall())

    cursor.close()
    conn.close()

    return {
        "quotation_chart": quotation_chart,
        "policy_chart": policy_chart,
        "claim_chart": claim_chart,
        "fraud_chart": fraud_chart,
        "vehicle_chart": vehicle_chart
    }



# RECENT CLAIMS
def get_recent_claim_data(limit=5):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            claim_number,
            customer_name,
            vehicle_type,
            brand,
            model,
            claim_status,
            fraud_risk,
            recommended_payout,
            created_at

        FROM claims

        ORDER BY created_at DESC

        LIMIT %s;
    """, (limit,))

    columns = [column[0] for column in cursor.description]

    data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return data

# RECENT QUOTATIONS

def get_recent_quotation_data(limit=5):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT

            q.quotation_id,

            cu.customer_name,

            q.vehicle_type,

            q.brand,

            q.model,

            q.policy_type,

            q.premium_amount,

            q.quotation_status,

            q.created_at

        FROM quotations q

        JOIN customers cu

        ON q.customer_id = cu.customer_id

        ORDER BY q.created_at DESC

        LIMIT %s;
    """, (limit,))

    columns = [column[0] for column in cursor.description]

    data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return data



# FRAUD SUMMARY

def get_fraud_summary_data():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT fraud_risk,
               COUNT(*)
        FROM claims
        GROUP BY fraud_risk;
    """)

    result = dict(cursor.fetchall())

    cursor.close()
    conn.close()

    return result


# LATEST AI ANALYSIS

def get_recent_ai_analysis(limit=5):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            claim_number,
            customer_name,
            vehicle_type,
            brand,
            model,
            fraud_risk,
            recommended_payout,
            created_at

        FROM claims

        ORDER BY created_at DESC

        LIMIT %s;
    """, (limit,))

    columns = [column[0] for column in cursor.description]

    result = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return result