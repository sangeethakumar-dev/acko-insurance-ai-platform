from backend.database.dashboard_queries import (
    get_dashboard_summary_data,
    get_dashboard_chart_data,
    get_recent_claim_data,
    get_recent_quotation_data,
    get_fraud_summary_data,
    get_recent_ai_analysis
)


# SUMMARY CARDS

def get_dashboard_summary():
    """
    Return dashboard summary cards.
    """
    return get_dashboard_summary_data()


# CHARTS

def get_dashboard_charts():
    """
    Return all dashboard charts.
    """
    return get_dashboard_chart_data()


# RECENT CLAIMS

def get_recent_claims(limit=5):
    """
    Return latest claims.
    """
    return get_recent_claim_data(limit)


# RECENT QUOTATIONS

def get_recent_quotations(limit=5):
    """
    Return latest quotations.
    """
    return get_recent_quotation_data(limit)


# FRAUD SUMMARY

def get_fraud_summary():
    """
    Return fraud statistics.
    """
    return get_fraud_summary_data()


# AI ANALYSIS

def get_ai_analysis(limit=5):
    """
    Return latest AI claim analysis.
    """
    return get_recent_ai_analysis(limit)



# COMPLETE DASHBOARD

def get_dashboard_data():
    """
    Returns all data required for the Admin Dashboard.
    This function is called by dashboard_router.py.
    """

    return {
        "summary": get_dashboard_summary(),
        "charts": get_dashboard_charts(),
        "recent_claims": get_recent_claims(),
        "recent_quotations": get_recent_quotations(),
        "fraud_summary": get_fraud_summary(),
        "recent_ai_analysis": get_ai_analysis()
    }