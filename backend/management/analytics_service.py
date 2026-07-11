from backend.database.analytics_queries import (
    get_monthly_revenue,
    get_claim_status_analytics,
    get_fraud_analytics,
    get_policy_analytics,
    get_vehicle_analytics,
    get_policy_type_analytics,
    get_claim_payout_analytics,
    get_customer_analytics,
    get_overall_analytics
)


# MONTHLY REVENUE

def get_monthly_revenue_service():
    """
    Return monthly premium revenue.
    """
    return get_monthly_revenue()


# CLAIM STATUS ANALYTICS

def get_claim_status_service():
    """
    Return claim status analytics.
    """
    return get_claim_status_analytics()


# FRAUD ANALYTICS

def get_fraud_analytics_service():
    """
    Return fraud analytics.
    """
    return get_fraud_analytics()


# POLICY ANALYTICS

def get_policy_analytics_service():
    """
    Return policy analytics.
    """
    return get_policy_analytics()


# VEHICLE ANALYTICS

def get_vehicle_analytics_service():
    """
    Return vehicle analytics.
    """
    return get_vehicle_analytics()


# POLICY TYPE ANALYTICS

def get_policy_type_service():
    """
    Return policy type analytics.
    """
    return get_policy_type_analytics()


# CLAIM PAYOUT

def get_claim_payout_service():
    """
    Return claim payout analytics.
    """
    return get_claim_payout_analytics()


# CUSTOMER ANALYTICS

def get_customer_analytics_service():
    """
    Return customer analytics.
    """
    return get_customer_analytics()


# COMPLETE ANALYTICS

def get_overall_analytics_service():
    """
    Return all analytics required for
    the Analytics Dashboard.
    """
    return get_overall_analytics()