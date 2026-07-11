from backend.database.quotation_queries import (
    get_all_quotations,
    get_quotation_by_id,
    search_quotations,
    update_quotation_status,
    delete_quotation,
    convert_to_policy
)

# GET ALL QUOTATIONS

def get_all_quotation_service():
    """
    Returns all quotations.
    """
    return get_all_quotations()


# GET QUOTATION BY ID

def get_quotation_service(quotation_id):
    """
    Returns a quotation by ID.
    """

    quotation = get_quotation_by_id(quotation_id)

    if quotation is None:
        raise ValueError("Quotation not found.")

    return quotation


# SEARCH QUOTATIONS

def search_quotation_service(keyword):
    """
    Search quotations.
    """

    if not keyword.strip():
        raise ValueError("Search keyword cannot be empty.")

    return search_quotations(keyword)


# UPDATE QUOTATION STATUS

def update_quotation_status_service(
    quotation_id,
    status
):
    """
    Update quotation status.
    """

    allowed_status = [
        "Pending",
        "Approved",
        "Rejected",
        "Bought"
    ]

    if status not in allowed_status:
        raise ValueError(
            f"Invalid quotation status: {status}"
        )

    update_quotation_status(
        quotation_id,
        status
    )

    return {
        "message": "Quotation status updated successfully."
    }


# DELETE QUOTATION

def delete_quotation_service(
    quotation_id
):
    """
    Delete quotation.
    """

    delete_quotation(quotation_id)

    return {
        "message": "Quotation deleted successfully."
    }


# CONVERT TO POLICY

def convert_quotation_to_policy_service(
    quotation_id,
    policy_number,
    start_date,
    expiry_date
):
    """
    Convert quotation into an insurance policy.
    """

    success = convert_to_policy(
        quotation_id,
        policy_number,
        start_date,
        expiry_date
    )

    if not success:
        raise ValueError(
            "Quotation not found."
        )

    return {
        "message": "Policy created successfully.",
        "policy_number": policy_number
    }


# APPROVE QUOTATION

def approve_quotation_service(
    quotation_id
):
    """
    Approve quotation.
    """

    update_quotation_status(
        quotation_id,
        "Approved"
    )

    return {
        "message": "Quotation approved successfully."
    }


# REJECT QUOTATION

def reject_quotation_service(
    quotation_id
):
    """
    Reject quotation.
    """

    update_quotation_status(
        quotation_id,
        "Rejected"
    )

    return {
        "message": "Quotation rejected successfully."
    }


# MARK AS BOUGHT

def mark_as_bought_service(
    quotation_id
):
    """
    Mark quotation as bought.
    """

    update_quotation_status(
        quotation_id,
        "Bought"
    )

    return {
        "message": "Quotation marked as bought."
    }