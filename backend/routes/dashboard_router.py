from fastapi import APIRouter, HTTPException

from backend.management.dashboard_service import (
    get_dashboard_data,
    get_dashboard_summary,
    get_dashboard_charts,
    get_recent_claims,
    get_recent_quotations,
    get_fraud_summary,
    get_ai_analysis
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Admin Dashboard"]
)


# COMPLETE DASHBOARD

@router.get("/")
def dashboard():
    """
    Returns complete dashboard data.
    """

    try:
        return get_dashboard_data()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# SUMMARY CARDS

@router.get("/summary")
def dashboard_summary():
    """
    Returns dashboard summary cards.
    """

    try:
        return get_dashboard_summary()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CHART DATA

@router.get("/charts")
def dashboard_charts():
    """
    Returns dashboard charts.
    """

    try:
        return get_dashboard_charts()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# RECENT CLAIMS

@router.get("/recent-claims")
def recent_claims(limit: int = 5):
    """
    Returns latest claims.
    """

    try:
        return get_recent_claims(limit)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# RECENT QUOTATIONS

@router.get("/recent-quotations")
def recent_quotations(limit: int = 5):
    """
    Returns latest quotations.
    """

    try:
        return get_recent_quotations(limit)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# FRAUD SUMMARY

@router.get("/fraud-summary")
def fraud_summary():
    """
    Returns fraud statistics.
    """

    try:
        return get_fraud_summary()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# AI CLAIM ANALYSIS

@router.get("/ai-analysis")
def ai_analysis(limit: int = 5):
    """
    Returns latest AI claim analysis.
    """

    try:
        return get_ai_analysis(limit)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )