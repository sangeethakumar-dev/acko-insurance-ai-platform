from datetime import date

from fastapi import APIRouter, HTTPException, Query

from backend.management.policy_service import (
    get_all_policy_service,
    get_policy_service,
    search_policy_service,
    update_policy_status_service,
    renew_policy_service,
    delete_policy_service,
    get_expiring_policy_service,
    activate_policy_service,
    expire_policy_service,
    cancel_policy_service
)

router = APIRouter(
    prefix="/policies",
    tags=["Policy Management"]
)


# GET ALL POLICIES

@router.get("/")
def get_all_policies():

    try:
        return get_all_policy_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# GET POLICY BY ID

@router.get("/{policy_id}")
def get_policy(policy_id: int):

    try:
        return get_policy_service(policy_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# SEARCH POLICIES

@router.get("/search/")
def search_policy(
    keyword: str = Query(...)
):

    try:
        return search_policy_service(keyword)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# UPDATE POLICY STATUS

@router.put("/{policy_id}/status")
def update_policy_status(
    policy_id: int,
    status: str
):

    try:
        return update_policy_status_service(
            policy_id,
            status
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ACTIVATE POLICY

@router.put("/{policy_id}/activate")
def activate_policy(
    policy_id: int
):

    try:
        return activate_policy_service(policy_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# EXPIRE POLICY

@router.put("/{policy_id}/expire")
def expire_policy(
    policy_id: int
):

    try:
        return expire_policy_service(policy_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CANCEL POLICY

@router.put("/{policy_id}/cancel")
def cancel_policy(
    policy_id: int
):

    try:
        return cancel_policy_service(policy_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# RENEW POLICY

@router.put("/{policy_id}/renew")
def renew_policy(
    policy_id: int,
    start_date: date,
    expiry_date: date
):

    try:
        return renew_policy_service(
            policy_id,
            start_date,
            expiry_date
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# EXPIRING POLICIES

@router.get("/expiring/")
def expiring_policies(
    days: int = 30
):

    try:
        return get_expiring_policy_service(days)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# DELETE POLICY

@router.delete("/{policy_id}")
def delete_policy(
    policy_id: int
):

    try:
        return delete_policy_service(policy_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )