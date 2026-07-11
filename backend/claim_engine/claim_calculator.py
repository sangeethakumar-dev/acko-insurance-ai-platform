
from typing import Dict, Any

# Depreciation Table
DEPRECIATION_TABLE = {
    1: 0.05,
    3: 0.15,
    5: 0.25,
    10: 0.40
}

# Policy Validation
def validate_policy(policy_type: str) -> bool:
    """
    Only Comprehensive policies are eligible.
    """

    if policy_type.lower() == "comprehensive":
        return True

    return False


# Vehicle Depreciation
def calculate_depreciation(
    vehicle_age: int,
    repair_cost: float,
    zero_dep: str
) -> float:
    """
    Calculate depreciation amount.
    """

    if zero_dep.lower() == "yes":
        return 0

    if vehicle_age <= 1:
        rate = DEPRECIATION_TABLE[1]

    elif vehicle_age <= 3:
        rate = DEPRECIATION_TABLE[3]

    elif vehicle_age <= 5:
        rate = DEPRECIATION_TABLE[5]

    else:
        rate = DEPRECIATION_TABLE[10]

    return repair_cost * rate


# Parts Cost
def calculate_parts_cost(
    repair_cost: float
) -> float:
    """
    Approximate OEM parts cost.

    Mentor UI:
    Parts Replacement ≈ 53%
    """

    return repair_cost * 0.53


# Labour Cost
def calculate_labour_cost(
    repair_cost: float
) -> float:
    """
    Labour & Refinishing

    Mentor UI:
    Labour ≈ 47%
    """

    return repair_cost * 0.47


# GST
def calculate_gst(
    parts_cost: float,
    labour_cost: float
) -> float:
    """
    GST = 18%
    """

    return (parts_cost + labour_cost) * 0.18


# Contingency Charges
def calculate_contingency(
    repair_cost: float
) -> float:
    """
    Miscellaneous clips,
    paint blending,
    consumables,
    fasteners etc.

    Approx 2%
    """

    return repair_cost * 0.02


# Previous Claims Deduction
def previous_claim_penalty(
    previous_claims: str,
    repair_cost: float
) -> float:

    if previous_claims.lower() == "none":
        return 0

    return repair_cost * 0.10


# No Claim Bonus Adjustment
def ncb_adjustment(
    ncb: str,
    repair_cost: float
) -> float:
    """
    Simple demo adjustment.
    """

    mapping = {
        "0%":0,
        "20%":0.02,
        "25%":0.03,
        "35%":0.04,
        "50%":0.05
    }

    rate = mapping.get(ncb,0)

    return repair_cost * rate


# Fraud Adjustment
def fraud_adjustment(
    fraud_risk: str
):

    fraud_risk = fraud_risk.upper()

    if fraud_risk == "LOW":

        return False, 0

    elif fraud_risk == "MEDIUM":

        return True, 0

    else:

        return True, 0.20
    


# Main Claim Calculation Engine
def calculate_claim(
    analysis: Dict[str, Any],
    claim_form: Dict[str, Any],
    fraud_result: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Main insurance claim calculation engine.

    Parameters
    ----------
    analysis : dict
        Output from image_analysis.py

    claim_form : dict
        User submitted claim details.

    fraud_result : dict
        Output from fraud_checker.py

    Returns
    -------
    dict
        Complete claim assessment.
    """

    
    # Read AI Analysis
    repair_cost = analysis.get("estimated_repair_cost", 0)
    severity = analysis.get("severity", 0)
    damage_type = analysis.get("damage_type", "")
    affected_parts = analysis.get("affected_parts", [])

    
    # Read User Inputs
    idv = claim_form.get("idv", 0)
    policy_type = claim_form.get("policy_type", "")
    vehicle_age = claim_form.get("vehicle_age", 0)
    zero_dep = claim_form.get("zero_dep", "No")
    previous_claims = claim_form.get("previous_claims", "None")
    ncb = claim_form.get("ncb", "0%")
    engine_protection = claim_form.get("engine_protection", "No")

    
    # Fraud Result
    fraud_risk = fraud_result.get("fraud_risk", "LOW")

    manual_review, fraud_deduction_rate = fraud_adjustment(
        fraud_risk
    )

    
    # Policy Validation
    if not validate_policy(policy_type):

        return {

            "approved": False,

            "coverage": "Rejected",

            "reason": "Policy is not eligible for own damage claim."
        }


    # Cost Breakdown
    parts_cost = calculate_parts_cost(
        repair_cost
    )

    labour_cost = calculate_labour_cost(
        repair_cost
    )

    gst = calculate_gst(
        parts_cost,
        labour_cost
    )

    contingency = calculate_contingency(
        repair_cost
    )

    depreciation = calculate_depreciation(
        vehicle_age,
        repair_cost,
        zero_dep
    )

    previous_penalty = previous_claim_penalty(
        previous_claims,
        repair_cost
    )

    ncb_penalty = ncb_adjustment(
        ncb,
        repair_cost
    )

    fraud_penalty = repair_cost * fraud_deduction_rate


    # Engine Protection
    engine_bonus = 0

    if engine_protection.lower() == "yes":

        engine_bonus = repair_cost * 0.05

    
    # Gross Claim
    gross_claim = (
        repair_cost
        + gst
        + contingency
        + engine_bonus
    )


    # Total Deductions
    total_deductions = (
        depreciation
        + previous_penalty
        + ncb_penalty
        + fraud_penalty
    )

    
    # Final Recommended Payout
    recommended_payout = gross_claim - total_deductions

    # Claim cannot exceed IDV

    if recommended_payout > idv:

        recommended_payout = idv

    if recommended_payout < 0:

        recommended_payout = 0


    # Remarks
    remarks = []

    if zero_dep.lower() == "yes":
        remarks.append(
            "Zero Depreciation benefit applied."
        )

    if engine_protection.lower() == "yes":
        remarks.append(
            "Engine Protection benefit applied."
        )

    if previous_claims.lower() == "none":
        remarks.append(
            "No previous claims."
        )
    else:
        remarks.append(
            "Previous claims considered."
        )

    remarks.append(
        f"Fraud Risk : {fraud_risk}"
    )

    if manual_review:
        remarks.append(
            "Manual survey recommended."
        )

    if severity >= 8:
        remarks.append(
            "High severity damage."
        )

    # Return Final Assessment
    return {

        "approved": True,

        "coverage": "Covered",

        "manual_review": manual_review,

        "vehicle_damage": damage_type,

        "affected_parts": affected_parts,

        "severity": severity,

        "repair_cost": round(repair_cost),

        "parts_cost": round(parts_cost),

        "labour_cost": round(labour_cost),

        "gst": round(gst),

        "contingency": round(contingency),

        "engine_bonus": round(engine_bonus),

        "depreciation": round(depreciation),

        "previous_claim_penalty": round(previous_penalty),

        "ncb_penalty": round(ncb_penalty),

        "fraud_penalty": round(fraud_penalty),

        "gross_claim": round(gross_claim),

        "total_deductions": round(total_deductions),

        "recommended_payout": round(recommended_payout),

        "remarks": remarks
    }


# Local Testing

if __name__ == "__main__":

    # Sample Gemini Analysis Output
    analysis = {

        "vehicle_type": "Car",

        "brand": "Kia",

        "model": "Sonet",

        "color": "White",

        "damage_type": "Front Bumper Damage",

        "severity": 4,

        "affected_parts": [

            "Front Bumper",

            "Fog Lamp",

            "Grille"

        ],

        "estimated_repair_cost": 18000

    }

    
    # Sample User Form
    claim_form = {

        "idv": 850000,

        "policy_type": "Comprehensive",

        "vehicle_age": 2,

        "zero_dep": "Yes",

        "engine_protection": "Yes",

        "previous_claims": "None",

        "ncb": "25%"

    }


    # Sample Fraud Result
    fraud_result = {

        "fraud_risk": "LOW",

        "fraud_score": 12,

        "flags": []

    }

    
    # Calculate Claim
    result = calculate_claim(

        analysis,

        claim_form,

        fraud_result

    )


    # Display Result
    print("\n========== CLAIM RESULT ==========\n")

    for key, value in result.items():

        print(f"{key} : {value}")