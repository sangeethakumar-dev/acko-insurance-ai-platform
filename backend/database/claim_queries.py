import uuid
from datetime import datetime

from backend.database.db import get_connection


# Generate Claim Number
def generate_claim_number():
    """
    Example:
    ACKO-2026-4F92AB
    """

    year = datetime.now().year

    random_code = str(uuid.uuid4())[:6].upper()

    return f"ACKO-{year}-{random_code}"


# Save Claim
def save_claim(

    customer_details: dict,

    analysis: dict,

    fraud_result: dict,

    claim_result: dict,

    image_paths: list

):
    conn = get_connection()

    cur = conn.cursor()

    claim_number = generate_claim_number()

    query = """
    INSERT INTO claims
    (

        claim_number,

        customer_name,

        vehicle_type,

        brand,

        model,

        policy_type,

        claim_status,

        fraud_risk,

        recommended_payout

    )

    VALUES

    (%s,%s,%s,%s,%s,%s,%s,%s,%s)

    RETURNING claim_id;
    """

    cur.execute(

        query,

        (

            claim_number,

            customer_details.get("customer_name"),

            analysis.get("vehicle_type"),

            analysis.get("brand"),

            analysis.get("model"),

            customer_details.get("policy_type"),

            "Submitted",

            fraud_result.get("fraud_risk"),

            claim_result.get("recommended_payout")

        )

    )

    claim_id = cur.fetchone()[0]

    # Save Uploaded Images

    image_query = """
INSERT INTO claim_images
(
    claim_id,
    image_path
)
VALUES
(%s,%s);
"""

    for image_path in image_paths:

        cur.execute(

        image_query,

        (

            claim_id,

            image_path

        )

    )


    conn.commit()

    cur.close()

    conn.close()

    return claim_id, claim_number


# Save Uploaded Images
def save_claim_images(

    claim_id,

    image_paths

):

    conn = get_connection()

    cur = conn.cursor()

    query = """

    INSERT INTO claim_images

    (

        claim_id,

        image_path

    )

    VALUES

    (%s,%s)

    """

    for image in image_paths:

        cur.execute(

            query,

            (

                claim_id,

                image

            )

        )

    conn.commit()

    cur.close()

    conn.close()

    conn = get_connection()

    cur = conn.cursor()

    query = """

    INSERT INTO claim_reports

    (

        claim_id,

        report

    )

    VALUES

    (%s,%s)

    """

    cur.execute(

        query,

        (

            claim_id,

            report

        )

    )

    conn.commit()

    cur.close()

    conn.close()



# Get Claim By Number


def get_claim(

    claim_number

):

    conn = get_connection()

    cur = conn.cursor()

    query = """

    SELECT *

    FROM claims

    WHERE claim_number=%s

    """

    cur.execute(

        query,

        (

            claim_number,

        )

    )

    result = cur.fetchone()

    cur.close()

    conn.close()

    return result


# Get All Claims
def get_all_claims():

    conn = get_connection()

    cur = conn.cursor()

    query = """

    SELECT *

    FROM claims

    ORDER BY created_at DESC

    """

    cur.execute(query)

    claims = cur.fetchall()

    cur.close()

    conn.close()

    return claims


#####################   Admin Claim Management Queries  ###############################


from backend.database.db import get_connection


# GET ALL CLAIMS (ADMIN)

def get_all_claims_admin():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            claim_id,
            claim_number,
            customer_name,
            vehicle_type,
            brand,
            model,
            policy_type,
            claim_status,
            fraud_risk,
            recommended_payout,
            created_at

        FROM claims

        ORDER BY created_at DESC;

    """)

    columns = [col[0] for col in cursor.description]

    result = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return result

# GET CLAIM DETAILS

def get_claim_by_id(claim_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM claims

        WHERE claim_id=%s;

    """, (claim_id,))

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

# SEARCH CLAIMS

def search_claims(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            claim_id,

            claim_number,

            customer_name,

            vehicle_type,

            claim_status,

            fraud_risk,

            recommended_payout

        FROM claims

        WHERE

            LOWER(claim_number) LIKE LOWER(%s)

            OR

            LOWER(customer_name) LIKE LOWER(%s)

            OR

            LOWER(vehicle_type) LIKE LOWER(%s)

        ORDER BY created_at DESC;

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


# UPDATE CLAIM STATUS

def update_claim_status(claim_id,status):

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        UPDATE claims

        SET claim_status=%s

        WHERE claim_id=%s;

    """,(status,claim_id))

    conn.commit()

    cursor.close()
    conn.close()

    return True


# GET CLAIM IMAGES

def get_claim_images(claim_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            image_path,

            uploaded_at

        FROM claim_images

        WHERE claim_id=%s;

    """, (claim_id,))

    columns = [col[0] for col in cursor.description]

    result = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()

    return result

# DELETE CLAIM

def delete_claim(claim_id):

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

        DELETE FROM claims

        WHERE claim_id=%s;

    """,(claim_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return True