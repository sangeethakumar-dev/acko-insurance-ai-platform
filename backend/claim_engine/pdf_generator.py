from pathlib import Path
from datetime import datetime
import uuid

from reportlab.lib import colors

from reportlab.lib.enums import (
    TA_CENTER,
    TA_LEFT
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.units import inch

from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle,

    PageBreak

)

from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

# Register Font

try:

    pdfmetrics.registerFont(
        TTFont(
            "Arial",
            "arial.ttf"
        )
    )

    DEFAULT_FONT = "Arial"

except:

    DEFAULT_FONT = "Helvetica"


# Create Styles
styles = getSampleStyleSheet()

TITLE_STYLE = ParagraphStyle(

    "Title",

    parent=styles["Heading1"],

    fontName=DEFAULT_FONT,

    fontSize=22,

    alignment=TA_CENTER,

    spaceAfter=25,

    textColor=colors.HexColor("#1E3A8A")

)

SECTION_STYLE = ParagraphStyle(

    "Section",

    parent=styles["Heading2"],

    fontName=DEFAULT_FONT,

    fontSize=15,

    textColor=colors.HexColor("#4F46E5"),

    spaceBefore=12,

    spaceAfter=8

)

BODY_STYLE = ParagraphStyle(

    "Body",

    parent=styles["BodyText"],

    fontName=DEFAULT_FONT,

    fontSize=10,

    leading=18,

    alignment=TA_LEFT

)

SMALL_STYLE = ParagraphStyle(

    "Small",

    parent=styles["BodyText"],

    fontName=DEFAULT_FONT,

    fontSize=8,

    textColor=colors.grey
)

# Header
def add_header(story):

    story.append(

        Paragraph(

            "AI INSURANCE CLAIM ASSESSMENT REPORT",

            TITLE_STYLE

        )

    )

    story.append(

        Paragraph(

            "ACKO AI Claims Engine",

            BODY_STYLE

        )

    )

    story.append(

        Spacer(

            1,

            0.2 * inch

        )

    )


# Claim Information
def add_claim_information(

    story,

    claim_result

):

    claim_number = (

        "ACKO-CLM-"

        + datetime.now().strftime("%Y")

        + "-"

        + str(uuid.uuid4())[:6].upper()

    )

    generated_date = datetime.now().strftime(

        "%d %B %Y"

    )

    data = [

        [

            "Claim Number",

            claim_number

        ],

        [

            "Generated Date",

            generated_date

        ],

        [

            "Status",

            "APPROVED"

            if claim_result["approved"]

            else "REJECTED"

        ],

        [

            "Coverage",

            claim_result["coverage"]

        ],

        [

            "Recommended Payout",

            f"₹ {claim_result['recommended_payout']:,}"

        ]

    ]

    table = Table(

        data,

        colWidths=[170,250]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(0,-1),

             colors.HexColor("#EEF2FF")),

            ("GRID",(0,0),(-1,-1),

             0.5,

             colors.grey),

            ("BOTTOMPADDING",

             (0,0),

             (-1,-1),

             10),

            ("FONTNAME",

             (0,0),

             (-1,-1),

             DEFAULT_FONT)

        ])

    )

    story.append(

        Paragraph(

            "Claim Information",

            SECTION_STYLE

        )

    )

    story.append(table)

    story.append(

        Spacer(

            1,

            0.25*inch

        )

    )


# Vehicle Information
def add_vehicle_information(

    story,

    analysis

):

    story.append(

        Paragraph(

            "Vehicle Information",

            SECTION_STYLE

        )

    )

    vehicle_table = [

        [

            "Vehicle Type",

            analysis.get(

                "vehicle_type",

                "Not Available"

            )

        ],

        [

            "Brand",

            analysis.get(

                "brand",

                "Not Available"

            )

        ],

        [

            "Model",

            analysis.get(

                "model",

                "Not Available"

            )

        ],

        [

            "Segment",

            analysis.get(

                "segment",

                "Not Available"

            )

        ],

        [

            "Color",

            analysis.get(

                "color",

                "Not Available"

            )

        ]

    ]

    table = Table(

        vehicle_table,

        colWidths=[170,250]

    )

    table.setStyle(

        TableStyle([

            ("GRID",

             (0,0),

             (-1,-1),

             0.5,

             colors.grey),

            ("BACKGROUND",

             (0,0),

             (0,-1),

             colors.HexColor("#EEF2FF")),

            ("BOTTOMPADDING",

             (0,0),

             (-1,-1),

             10),

            ("FONTNAME",

             (0,0),

             (-1,-1),

             DEFAULT_FONT)

        ])

    )

    story.append(table)

    story.append(

        Spacer(

            1,

            0.25*inch

        )

    )

# Executive Summary
def add_executive_summary(
    story,
    report_text
):

    story.append(
        Paragraph(
            "1. Executive Summary",
            SECTION_STYLE
        )
    )

    story.append(
        Paragraph(
            report_text,
            BODY_STYLE
        )
    )

    story.append(
        Spacer(
            1,
            0.25 * inch
        )
    )


# Damage Assessment
def add_damage_assessment(
    story,
    analysis
):

    story.append(
        Paragraph(
            "2. Damage Assessment",
            SECTION_STYLE
        )
    )

    damage_table = [

        [
            "Damage Type",
            analysis.get(
                "damage_type",
                "Not Available"
            )
        ],

        [
            "Severity",
            f"{analysis.get('severity',0)}/10"
        ],

        [
            "Affected Parts",
            ", ".join(
                analysis.get(
                    "affected_parts",
                    []
                )
            ) or "None"
        ],

        [
            "Estimated Repair Cost",
            f"₹ {analysis.get('estimated_repair_cost',0):,}"
        ]

    ]

    table = Table(
        damage_table,
        colWidths=[170,250]
    )

    table.setStyle(
        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),
             colors.HexColor("#EEF2FF")),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("FONTNAME",(0,0),(-1,-1),DEFAULT_FONT)

        ])
    )

    story.append(table)

    story.append(
        Spacer(
            1,
            0.25*inch
        )
    )


# Coverage Analysis
def add_coverage_analysis(
    story,
    customer_details,
    claim_result
):

    story.append(
        Paragraph(
            "3. Coverage Analysis",
            SECTION_STYLE
        )
    )

    coverage = f"""

Policy Type :
<b>{customer_details.get('policy_type','Not Available')}</b>

Policy Age :
<b>{customer_details.get('policy_age','Not Available')}</b>

Zero Depreciation :
<b>{customer_details.get('zero_dep','No')}</b>

Engine Protection :
<b>{customer_details.get('engine_protection','No')}</b>

Previous Claims :
<b>{customer_details.get('previous_claims','None')}</b>

No Claim Bonus :
<b>{customer_details.get('ncb','0%')}</b>

Coverage Decision :
<b>{claim_result.get('coverage','Covered')}</b>

"""

    story.append(
        Paragraph(
            coverage,
            BODY_STYLE
        )
    )

    story.append(
        Spacer(
            1,
            0.25*inch
        )
    )



# Fraud Analysis
def add_fraud_analysis(
    story,
    fraud_result
):

    story.append(
        Paragraph(
            "4. Fraud Assessment",
            SECTION_STYLE
        )
    )

    fraud_table = [

        [
            "Fraud Risk",
            fraud_result.get(
                "fraud_risk",
                "LOW"
            )
        ],

        [
            "Fraud Score",
            str(
                fraud_result.get(
                    "fraud_score",
                    0
                )
            )
        ],

        [
            "Flags",
            ", ".join(
                fraud_result.get(
                    "flags",
                    []
                )
            ) or "None"
        ]

    ]

    table = Table(
        fraud_table,
        colWidths=[170,250]
    )

    table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),
             0.5,
             colors.grey),

            ("BACKGROUND",
             (0,0),
             (0,-1),
             colors.HexColor("#EEF2FF")),

            ("BOTTOMPADDING",
             (0,0),
             (-1,-1),
             10),

            ("FONTNAME",
             (0,0),
             (-1,-1),
             DEFAULT_FONT)

        ])

    )

    story.append(table)

    story.append(
        Spacer(
            1,
            0.25*inch
        )
    )


# Repair Cost Breakdown
def add_cost_breakdown(
    story,
    claim_result
):

    story.append(
        Paragraph(
            "5. Repair Cost Breakdown",
            SECTION_STYLE
        )
    )

    data = [

        [

            "Description",

            "Amount (₹)"

        ],

        [

            "Parts Replacement",

            f"{claim_result.get('parts_cost',0):,}"

        ],

        [

            "Professional Labour & Refinishing",

            f"{claim_result.get('labour_cost',0):,}"

        ],

        [

            "GST",

            f"{claim_result.get('gst',0):,}"

        ],

        [

            "Contingency",

            f"{claim_result.get('contingency',0):,}"

        ],

        [

            "Depreciation",

            f"{claim_result.get('depreciation',0):,}"

        ],

        [

            "Previous Claim Deduction",

            f"{claim_result.get('previous_claim_penalty',0):,}"

        ],

        [

            "NCB Adjustment",

            f"{claim_result.get('ncb_penalty',0):,}"

        ],

        [

            "Fraud Adjustment",

            f"{claim_result.get('fraud_penalty',0):,}"

        ],

        [

            "<b>Total Recommended Payout</b>",

            f"<b>₹ {claim_result.get('recommended_payout',0):,}</b>"

        ]

    ]

    table = Table(

        data,

        colWidths=[300,120]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",
             (0,0),
             (-1,0),
             colors.HexColor("#4338CA")),

            ("TEXTCOLOR",
             (0,0),
             (-1,0),
             colors.white),

            ("GRID",
             (0,0),
             (-1,-1),
             0.5,
             colors.grey),

            ("BACKGROUND",
             (0,-1),
             (-1,-1),
             colors.HexColor("#DCFCE7")),

            ("FONTNAME",
             (0,0),
             (-1,-1),
             DEFAULT_FONT),

            ("BOTTOMPADDING",
             (0,0),
             (-1,-1),
             10)

        ])

    )

    story.append(table)

    story.append(
        Spacer(
            1,
            0.30*inch
        )
    )


# Claim Decision
def add_claim_decision(
    story,
    claim_result
):

    story.append(
        Paragraph(
            "6. Claim Decision",
            SECTION_STYLE
        )
    )

    status = (
        "APPROVED"
        if claim_result.get("approved")
        else "REJECTED"
    )

    color = (
        "#16A34A"
        if claim_result.get("approved")
        else "#DC2626"
    )

    decision_style = ParagraphStyle(

        "Decision",

        parent=BODY_STYLE,

        alignment=TA_CENTER,

        fontSize=16,

        textColor=colors.HexColor(color),

        spaceAfter=15

    )

    story.append(
        Paragraph(
            f"<b>{status}</b>",
            decision_style
        )
    )

    story.append(
        Spacer(
            1,
            0.20*inch
        )
    )


# Recommendations
def add_recommendations(
    story,
    claim_result
):

    story.append(
        Paragraph(
            "7. Recommendations",
            SECTION_STYLE
        )
    )

    remarks = claim_result.get("remarks", [])

    if not remarks:

        remarks = [

            "No additional recommendations."

        ]

    for remark in remarks:

        story.append(

            Paragraph(

                f"• {remark}",

                BODY_STYLE

            )

        )

    story.append(

        Spacer(

            1,

            0.25*inch

        )

    )


# Next Steps
def add_next_steps(
    story
):

    story.append(
        Paragraph(
            "8. Next Steps",
            SECTION_STYLE
        )
    )

    steps = [

        "Visit the nearest authorised network workshop.",

        "Carry your Claim ID and policy documents.",

        "Workshop will inspect the vehicle.",

        "Repairs will begin after approval.",

        "Payment will be settled according to the approved amount."

    ]

    for step in steps:

        story.append(

            Paragraph(

                f"• {step}",

                BODY_STYLE

            )

        )

    story.append(

        Spacer(

            1,

            0.25*inch

        )

    )


# Disclaimer
def add_disclaimer(
    story
):

    story.append(
        Paragraph(
            "9. Disclaimer",
            SECTION_STYLE
        )
    )

    disclaimer = """

This assessment was generated using AI-assisted image analysis and
insurance claim evaluation.

The estimated repair cost, fraud assessment, and recommended payout
are advisory in nature.

Final approval is subject to inspection and verification by the
insurance company's authorised surveyor.

"""

    story.append(
        Paragraph(
            disclaimer,
            BODY_STYLE
        )
    )

    story.append(
        Spacer(
            1,
            0.30*inch
        )
    )

# Footer
def add_footer(
    story
):

    story.append(

        Paragraph(

            "<b>Authorised By</b>",

            SECTION_STYLE

        )

    )

    story.append(

        Paragraph(

            "Senior Claims Surveyor",

            BODY_STYLE

        )

    )

    story.append(

        Paragraph(

            "AI Insurance Claim Engine",

            BODY_STYLE

        )

    )

    story.append(

        Spacer(

            1,

            0.25*inch

        )

    )

    story.append(

        Paragraph(

            "This document is system generated.",

            SMALL_STYLE

        )

    )

    story.append(

        Paragraph(

            "© 2026 AI Insurance Platform",

            SMALL_STYLE

        )

    )

