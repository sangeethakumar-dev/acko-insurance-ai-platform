from backend.database.claim_queries import (
    get_all_claims_admin,
    get_claim_by_id,
    search_claims,
    update_claim_status,
    get_claim_images,
    get_claim_analysis,
    delete_claim
)


# GET ALL CLAIMS

def get_all_claim_service():
    """
    Return all insurance claims.
    """
    return get_all_claims_admin()


# GET CLAIM BY ID

def get_claim_service(claim_id):
    """
    Return claim details.
    """

    claim = get_claim_by_id(claim_id)

    if claim is None:
        raise ValueError("Claim not found.")

    return claim



# SEARCH CLAIMS

def search_claim_service(keyword):
    """
    Search claims.
    """

    if not keyword.strip():
        raise ValueError("Search keyword cannot be empty.")

    return search_claims(keyword)


# UPDATE CLAIM STATUS

def update_claim_status_service(
    claim_id,
    status
):
    """
    Update claim status.
    """

    allowed_status = [
        "Pending",
        "Approved",
        "Rejected"
    ]

    if status not in allowed_status:
        raise ValueError(
            f"Invalid claim status: {status}"
        )

    update_claim_status(
        claim_id,
        status
    )

    return {
        "message": "Claim status updated successfully."
    }


# APPROVE CLAIM

def approve_claim_service(claim_id):
    """
    Approve claim.
    """

    update_claim_status(
        claim_id,
        "Approved"
    )

    return {
        "message": "Claim approved successfully."
    }


# REJECT CLAIM

def reject_claim_service(claim_id):
    """
    Reject claim.
    """

    update_claim_status(
        claim_id,
        "Rejected"
    )

    return {
        "message": "Claim rejected successfully."
    }


# GET CLAIM IMAGES

def get_claim_images_service(claim_id):
    """
    Return uploaded images for a claim.
    """

    return get_claim_images(claim_id)


# GET AI ANALYSIS

def get_claim_analysis_service(claim_id):
    """
    Return AI damage analysis.
    """

    analysis = get_claim_analysis(claim_id)

    if analysis is None:
        raise ValueError("AI analysis not found.")

    return analysis


# COMPLETE CLAIM DETAILS

def get_complete_claim_service(claim_id):
    """
    Return complete claim information.
    """

    claim = get_claim_by_id(claim_id)

    if claim is None:
        raise ValueError("Claim not found.")

    return {

        "claim": claim,

        "images": get_claim_images(claim_id),

        "analysis": get_claim_analysis(claim_id)

    }


# DELETE CLAIM

def delete_claim_service(claim_id):
    """
    Delete claim.
    """

    delete_claim(claim_id)

    return {
        "message": "Claim deleted successfully."
    }


# GET PENDING CLAIMS

def get_pending_claims_service():
    """
    Return all pending claims.
    """

    claims = get_all_claims_admin()

    return [
        claim
        for claim in claims
        if claim["claim_status"] == "Pending"
    ]


# GET APPROVED CLAIMS

def get_approved_claims_service():
    """
    Return all approved claims.
    """

    claims = get_all_claims_admin()

    return [
        claim
        for claim in claims
        if claim["claim_status"] == "Approved"
    ]


# GET REJECTED CLAIMS

def get_rejected_claims_service():
    """
    Return all rejected claims.
    """

    claims = get_all_claims_admin()

    return [
        claim
        for claim in claims
        if claim["claim_status"] == "Rejected"
    ]