from typing import Dict, Any, List

def build_prompt(user_query, top_3_chunks):
    context = ""

    for score, chunk, metadata in top_3_chunks:
        context += f"""
        Source: {metadata['pdf_name']}
        Section: {metadata.get('section_title', metadata.get('section', 'N/A'))}

        {chunk}

        """
    
    prompt = f"""
        You are Acko Insurance AI Assistant.

        Answer the user's insurance-related questions using ONLY the provided context.

        Rules:
        1.Do not use external knowledge.
        2.Do not make assumptions.
        3.Only answer from provided context.
        4. If answer is not available, say:
        "Sorry, I couldn't find this information in the policy documents."
        5. Be clear and concise.
        6. Mention policy details when relevant.
        7. Give response in simple user-friendly language.
        8. If possible, mention which policy document the answer came from.
        Context:
            {context}
        User Question:
            {user_query}
            """
    return prompt


def build_quote_prompt(insurance_type, details: dict, predicted_premium: float):

    prompt = f"""
You are ACKO Insurance AI Assistant.

The user requested an insurance quotation.

Customer Details:

Customer Age: {details['customer_age']}
City: {details['city']}
State: {details['state']}
Vehicle Make: {details['vehicle_make']}
Vehicle Model: {details['vehicle_model']}
Variant: {details['variant']}
Fuel Type: {details['fuel_type']}
Manufacturing Year: {details['manufacturing_year']}
Engine CC: {details['engine_cc']}
Vehicle Age: {details['vehicle_age_years']} years
IDV: ₹{details['idv']}
NCB: {details['ncb_percent']}%
Previous Claims: {details['claim_history_count']}
Policy Type: {details['policy_type']}
Usage Type: {details['usage_type']}
Number of Add-ons: {details['num_addons']}

Machine Learning Estimated Annual Premium

₹{predicted_premium:,.2f}

Now explain this quotation to the customer.

Include:

• Estimated Annual Premium
• Monthly equivalent premium
• Why this premium is estimated
• How IDV affects premium
• How NCB affects premium
• Mention claim history impact
• Mention this is an AI estimation
• End politely

Keep the response under 150 words.

Explain:

1. Estimated premium
2. Why this premium was predicted
3. Factors increasing premium
4. Factors reducing premium
5. Suggest ways to reduce premium in future

Keep it friendly.
Do not invent numbers.
"""

    return prompt

def build_claim_analysis_prompt() -> str:
    """
    Prompt for Gemini Vision.
    Image(s) will be supplied separately.
    """

    return """
You are an expert Motor Insurance Surveyor.

Analyze the uploaded vehicle damage images.

Return ONLY valid JSON.

Required JSON format:

{
    "vehicle_type":"",
    "brand":"",
    "model":"",
    "color":"",
    "segment":"",
    "incident_type":"",
    "damage_type":"",
    "severity":0,
    "affected_parts":[],
    "estimated_repair_cost":0,
    "fraud_risk":"",
    "summary":""
}

Rules:

- Detect vehicle type.
- Detect brand.
- Detect model if visible.
- Detect color.
- Detect damage type.
- Detect damaged parts.
- Give severity from 1 to 10.
- Estimate repair cost in INR.
- Mention fraud risk as LOW, MEDIUM or HIGH.
- Return ONLY JSON.
"""


def build_claim_report_prompt(claim_data: Dict[str, Any]) -> str:
    return f"""
You are a Senior Motor Insurance Claims Surveyor working for a leading insurance company.

Your responsibility is to prepare a professional claim assessment report after reviewing:

• Vehicle information
• AI image damage analysis
• Policy details
• Fraud analysis
• Claim calculation

Below is the complete claim information.

{claim_data}


===========================
REPORT REQUIREMENTS
===========================

Generate a professional insurance report.

Use clear headings.

Do NOT use markdown.

Write in a formal insurance company style.

The report must contain ALL of the following sections.


==================================================
CLAIM ASSESSMENT REPORT
==================================================

Claim Number:
Claim Date:
Assessment Status:

--------------------------------------------------

1. EXECUTIVE SUMMARY

Summarize

• vehicle involved

• type of accident

• damage severity

• overall recommendation

Write 1-2 professional paragraphs.


--------------------------------------------------

2. VEHICLE INFORMATION

Include

Vehicle Type

Brand

Model

Segment

Color

Insurance Declared Value (IDV)

Policy Type


--------------------------------------------------

3. DAMAGE ASSESSMENT

Describe

Damage Type

Severity Score (1-10)

Affected Parts

Estimated Repair Cost

Explain how the damage appears from the uploaded images.


--------------------------------------------------

4. COVERAGE ANALYSIS

Explain

Is the damage covered?

Why?

Mention

Policy Type

Zero Depreciation

Engine Protection

Previous Claims

No Claim Bonus

Explain how each affects the claim.


--------------------------------------------------

5. FRAUD ASSESSMENT

Mention

Fraud Risk

Fraud Score

Detected Flags

Explain why the claim appears

LOW

MEDIUM

or

HIGH

risk.


--------------------------------------------------

6. REPAIR COST BREAKDOWN

Display the following as a table.

Description                     Amount (INR)

Parts Replacement

Labour & Refinishing

GST

Miscellaneous / Contingency

Depreciation

Previous Claim Deduction

NCB Adjustment

Fraud Deduction

--------------------------------------------------

Gross Claim Amount

Recommended Payout


--------------------------------------------------

7. CLAIM DECISION

Clearly state

APPROVED

or

REJECTED

If manual inspection is required,

mention it.


--------------------------------------------------

8. RECOMMENDATIONS

Provide professional recommendations for

repair

inspection

customer

insurance company


--------------------------------------------------

9. NEXT STEPS

Explain what the customer should do next.

Example

• Visit network garage

• Carry policy documents

• Submit ID proof

• Wait for approval

• Download report


--------------------------------------------------

10. DISCLAIMER

Mention that

"This assessment is AI-assisted and subject to final approval by the insurance company's surveyor."


==================================================
WRITING STYLE
==================================================

Write professionally.

Avoid bullet overload.

Sound like an official insurance company report.

Return ONLY the report.

Do not return JSON.

Do not return Markdown.

Do not explain your reasoning.
"""

def build_manager_prompt(question: str, context: str) -> str:

    return f"""
You are an AI Insurance Manager.

Use the dashboard data below.

Dashboard Data:

{context}

Manager Question:

{question}

Answer clearly and professionally.
"""

