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


def build_quote_prompt(
    insurance_type,
    details: dict,
    predicted_premium: float
):

    return f"""
You are an ACKO Insurance AI Advisor.

The machine learning model has already predicted the annual premium.

DO NOT change the premium amount.

Predicted Annual Premium:
₹{predicted_premium:,.2f}

Vehicle Details

Vehicle Make : {details['vehicle_make']}
Vehicle Model : {details['vehicle_model']}
Variant : {details['variant']}
Fuel Type : {details['fuel_type']}
Manufacturing Year : {details['manufacturing_year']}
Vehicle Age : {details['vehicle_age_years']}
Engine CC : {details['engine_cc']}
IDV : ₹{details['idv']}

Policy Details

Policy Type : {details['policy_type']}
NCB : {details['ncb_percent']}%
Previous Claims : {details['claim_history_count']}
Add-ons : {details['num_addons']}

Customer Details

Age : {details['customer_age']}
City : {details['city']}
State : {details['state']}

Write ONLY HTML.

Do NOT use Markdown.

Do NOT use ** or #.

Do NOT use triple backticks.

Keep the response below 170 words.

Use this structure exactly:

<h3>Understanding Your Quote</h3>

<ul>

<li><b>Premium Factors:</b> Explain why the premium has this value.</li>

<li><b>NCB Impact:</b> Explain how NCB affects premium.</li>

<li><b>Claim History:</b> Explain previous claims effect.</li>

<li><b>IDV:</b> Explain how IDV affects premium.</li>

<li><b>Policy Coverage:</b> Mention the selected policy type.</li>

<li><b>Ways to Reduce Premium:</b> Give 3 short tips.</li>

</ul>

End with one short recommendation.

Never change the predicted premium.
"""



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

def build_claim_report_prompt(claim_data):

    return f"""
You are an insurance claim assessor.

Using the following claim details:

{claim_data}

Generate a short professional claim summary.

Include:

1. Claim Status (Approved / Rejected)
2. Vehicle Details
3. Damage Summary
4. Estimated Repair Cost
5. Recommended Claim Amount
6. Fraud Risk
7. Key Remarks
8. Next Step for Customer

Use simple professional language.

Do not use markdown.

Return only the report.
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

