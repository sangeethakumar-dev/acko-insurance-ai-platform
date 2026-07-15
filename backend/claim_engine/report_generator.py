from backend.utils.gemini_client import gemini_client
from backend.utils.prompt_builder import build_claim_report_prompt

def format_claim_data(claim_data: dict) -> str:
    """
    Convert claim dictionary into a structured text
    before sending it to Gemini.
    """

    vehicle = claim_data.get("vehicle_information", {})
    damage = claim_data.get("damage_assessment", {})
    fraud = claim_data.get("fraud_analysis", {})
    claim = claim_data.get("claim_assessment", {})
    customer = claim_data.get("customer_details", {})

    return f"""
====================================================
VEHICLE INFORMATION
====================================================

Vehicle Type      : {vehicle.get("vehicle_type", "Not Available")}
Brand             : {vehicle.get("brand", "Not Available")}
Model             : {vehicle.get("model", "Not Available")}
Segment           : {vehicle.get("segment", "Not Available")}
Color             : {vehicle.get("color", "Not Available")}

====================================================
DAMAGE ASSESSMENT
====================================================

Damage Type       : {damage.get("damage_type", "Not Available")}
Severity Score    : {damage.get("severity", 0)}/10

Affected Parts

{", ".join(damage.get("affected_parts", []))}

Estimated Repair Cost

₹{damage.get("repair_cost", 0)}

====================================================
POLICY INFORMATION
====================================================

Policy Type           : {customer.get("policy_type", "Not Available")}
Policy Age            : {customer.get("policy_age", "Not Available")}
State                 : {customer.get("state", "Not Available")}
Annual Premium        : ₹{customer.get("annual_premium", 0)}
Previous Claims       : {customer.get("previous_claims", "None")}
No Claim Bonus        : {customer.get("ncb", "0%")}
Zero Depreciation     : {customer.get("zero_dep", "No")}
Engine Protection     : {customer.get("engine_protection", "No")}
Age Group             : {customer.get("age_group", "Not Available")}
City Tier             : {customer.get("city_tier", "Not Available")}

====================================================
FRAUD ANALYSIS
====================================================

Fraud Risk

{fraud.get("fraud_risk", "LOW")}

Fraud Score

{fraud.get("fraud_score", 0)}

Flags

{", ".join(fraud.get("flags", [])) or "None"}

====================================================
CLAIM CALCULATION
====================================================

Coverage

{claim.get("coverage")}
Repair Cost

₹{claim.get("repair_cost", 0)}

Parts Cost

₹{claim.get("parts_cost", 0)}

Labour Cost

₹{claim.get("labour_cost", 0)}

GST

₹{claim.get("gst", 0)}

Contingency

₹{claim.get("contingency", 0)}

Depreciation

₹{claim.get("depreciation", 0)}

Previous Claim Penalty

₹{claim.get("previous_claim_penalty", 0)}

NCB Penalty

₹{claim.get("ncb_penalty", 0)}

Fraud Penalty

₹{claim.get("fraud_penalty", 0)}

Gross Claim

₹{claim.get("gross_claim", 0)}

Recommended Payout

₹{claim.get("recommended_payout", 0)}

Manual Review

{claim.get("manual_review", False)}

====================================================
REMARKS
====================================================

{chr(10).join("- " + remark for remark in claim.get("remarks", [])) or "No remarks available."}

"""



def generate_claim_report(
    analysis: dict,
    fraud_result: dict,
    claim_result: dict,
    customer_details: dict
):

    claim_data = {

    "vehicle_information": {

        "vehicle_type": analysis.get("vehicle_type"),
        "brand": analysis.get("brand"),
        "model": analysis.get("model"),
        "color": analysis.get("color"),
        "segment": analysis.get("segment")

    },

    "damage_assessment": {

        "damage_type": analysis.get("damage_type"),
        "severity": analysis.get("severity"),
        "affected_parts": analysis.get("affected_parts"),
        "repair_cost": analysis.get("estimated_repair_cost")

    },

    "fraud_analysis": fraud_result,

    "claim_assessment": claim_result,

    "customer_details": customer_details

}   

    formatted_claim_data = format_claim_data(claim_data)

    prompt = build_claim_report_prompt(formatted_claim_data)

    response = gemini_client.models.generate_content(

        model="gemini-flash-latest",

        contents=prompt

    )

    return response.text