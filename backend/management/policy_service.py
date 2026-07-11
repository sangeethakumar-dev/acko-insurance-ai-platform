from backend.database.policy_queries import (
    get_all_policies,
    get_policy_by_id,
    search_policies,
    update_policy_status,
    renew_policy,
    delete_policy,
    get_expiring_policies
)


# GET ALL POLICIES

def get_all_policy_service():
    """
    Return all insurance policies.
    """
    return get_all_policies()


# GET POLICY BY ID

def get_policy_service(policy_id):
    """
    Return a single policy.
    """

    policy = get_policy_by_id(policy_id)

    if policy is None:
        raise ValueError("Policy not found.")

    return policy


# SEARCH POLICIES

def search_policy_service(keyword):
    """
    Search policies.
    """

    if not keyword.strip():
        raise ValueError("Search keyword cannot be empty.")

    return search_policies(keyword)


# UPDATE POLICY STATUS

def update_policy_status_service(
    policy_id,
    status
):
    """
    Update policy status.
    """

    allowed_status = [
        "Active",
        "Expired",
        "Cancelled"
    ]

    if status not in allowed_status:
        raise ValueError(
            f"Invalid policy status: {status}"
        )

    update_policy_status(
        policy_id,
        status
    )

    return {
        "message": "Policy status updated successfully."
    }


# RENEW POLICY

def renew_policy_service(
    policy_id,
    start_date,
    expiry_date
):
    """
    Renew an existing insurance policy.
    """

    renew_policy(
        policy_id,
        start_date,
        expiry_date
    )

    return {
        "message": "Policy renewed successfully."
    }


# DELETE POLICY

def delete_policy_service(
    policy_id
):
    """
    Delete a policy.
    """

    delete_policy(policy_id)

    return {
        "message": "Policy deleted successfully."
    }


# GET EXPIRING POLICIES

def get_expiring_policy_service(
    days=30
):
    """
    Return policies that expire within
    the specified number of days.
    """

    return get_expiring_policies(days)


# ACTIVATE POLICY

def activate_policy_service(
    policy_id
):
    """
    Activate a policy.
    """

    update_policy_status(
        policy_id,
        "Active"
    )

    return {
        "message": "Policy activated successfully."
    }


# EXPIRE POLICY

def expire_policy_service(
    policy_id
):
    """
    Mark policy as expired.
    """

    update_policy_status(
        policy_id,
        "Expired"
    )

    return {
        "message": "Policy marked as expired."
    }


# CANCEL POLICY

def cancel_policy_service(
    policy_id
):
    """
    Cancel an insurance policy.
    """

    update_policy_status(
        policy_id,
        "Cancelled"
    )

    return {
        "message": "Policy cancelled successfully."
    }