from fastapi import APIRouter, HTTPException, Query

from backend.management.customer_service import (
    get_all_customer_service,
    get_customer_service,
    search_customer_service,
    get_customer_policies_service,
    get_customer_claims_service,
    get_customer_statistics_service,
    get_customer_profile_service,
    delete_customer_service
)

router = APIRouter(
    prefix="/customers",
    tags=["Customer Management"]
)


# GET ALL CUSTOMERS

@router.get("/")
def get_all_customers():

    try:
        return get_all_customer_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# GET CUSTOMER BY ID

@router.get("/{customer_id}")
def get_customer(customer_id: int):

    try:
        return get_customer_service(customer_id)

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


# GET COMPLETE CUSTOMER PROFILE

@router.get("/{customer_id}/profile")
def get_customer_profile(customer_id: int):

    try:
        return get_customer_profile_service(customer_id)

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


# SEARCH CUSTOMERS

@router.get("/search/")
def search_customer(
    keyword: str = Query(...)
):

    try:
        return search_customer_service(keyword)

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


# GET CUSTOMER POLICIES

@router.get("/{customer_id}/policies")
def customer_policies(customer_id: int):

    try:
        return get_customer_policies_service(customer_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# GET CUSTOMER CLAIMS

@router.get("/{customer_id}/claims")
def customer_claims(customer_id: int):

    try:
        return get_customer_claims_service(customer_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# GET CUSTOMER STATISTICS

@router.get("/{customer_id}/statistics")
def customer_statistics(customer_id: int):

    try:
        return get_customer_statistics_service(customer_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# DELETE CUSTOMER

@router.delete("/{customer_id}")
def delete_customer(customer_id: int):

    try:
        return delete_customer_service(customer_id)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )