from fastapi import APIRouter, HTTPException

from backend.management.analytics_service import (
    get_monthly_revenue_service,
    get_claim_status_service,
    get_fraud_analytics_service,
    get_policy_analytics_service,
    get_vehicle_analytics_service,
    get_policy_type_service,
    get_claim_payout_service,
    get_customer_analytics_service,
    get_overall_analytics_service
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# OVERALL ANALYTICS

@router.get("/")
def get_all_analytics():

    try:
        return get_overall_analytics_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# MONTHLY REVENUE

@router.get("/revenue")
def monthly_revenue():

    try:
        return get_monthly_revenue_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CLAIM STATUS

@router.get("/claims")
def claim_status():

    try:
        return get_claim_status_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# FRAUD ANALYTICS

@router.get("/fraud")
def fraud_analytics():

    try:
        return get_fraud_analytics_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# POLICY ANALYTICS

@router.get("/policies")
def policy_analytics():

    try:
        return get_policy_analytics_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# VEHICLE ANALYTICS

@router.get("/vehicles")
def vehicle_analytics():

    try:
        return get_vehicle_analytics_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# POLICY TYPE ANALYTICS

@router.get("/policy-types")
def policy_type_analytics():

    try:
        return get_policy_type_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CLAIM PAYOUT

@router.get("/claim-payout")
def claim_payout():

    try:
        return get_claim_payout_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CUSTOMER ANALYTICS

@router.get("/customers")
def customer_analytics():

    try:
        return get_customer_analytics_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )