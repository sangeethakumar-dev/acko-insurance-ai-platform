
from typing import Dict, Any

"""
Analyze fraud risk based on Gemini image analysis.

Parameters
    analysis : dict
        Output from image_analysis.py

Returns
    dict
        Fraud assessment.
"""

def analyze_fraud(analysis: Dict[str, Any]) -> Dict[str, Any]:
    score = 0

    flags = []

    severity = analysis.get("severity", 0)

    repair_cost = analysis.get(
        "estimated_repair_cost",
        0
    )

    brand = analysis.get("brand", "")

    model = analysis.get("model", "")

    summary = analysis.get(
        "summary",
        ""
    ).lower()

    # Rule 1
    if severity >= 8:
        score += 30
        flags.append(
            "Very severe damage."
        )

    # Rule 2
    if repair_cost >= 150000:
        score += 25
        flags.append(
            "Very high repair estimate."
        )


    # Rule 3
    if brand == "":
        score += 15
        flags.append(
            "Vehicle brand not detected."
        )

    # Rule 4
    if model == "":
        score += 10
        flags.append(
            "Vehicle model not detected."
        )

    # Rule 5
    suspicious_words = [
        "unclear",
        "cannot determine",
        "blur",
        "hidden",
        "poor quality"
    ]

    for word in suspicious_words:

        if word in summary:

            score += 10

            flags.append(
                "Poor image quality."
            )

            break

    # Risk Level
    if score <= 20:

        risk = "LOW"

    elif score <= 50:

        risk = "MEDIUM"

    else:

        risk = "HIGH"

    return {

        "fraud_score": score,

        "fraud_risk": risk,

        "flags": flags
    }