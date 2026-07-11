from backend.claim_engine.image_validator import validate_uploaded_images
from backend.claim_engine.image_analysis import analyze_images
from backend.claim_engine.fraud_checker import analyze_fraud
from backend.claim_engine.claim_calculator import calculate_claim
from backend.claim_engine.report_generator import generate_claim_report
from backend.claim_engine.pdf_generator import generate_claim_pdf

from backend.database.claim_queries import save_claim

import os
from pathlib import Path
from fastapi import UploadFile


async def process_claim(
        image: UploadFile,
        customer_details
):

    # Step 1 : Validate Images

    validation = await validate_uploaded_images(image)

    if not validation["valid"]:

        return validation
    
    os.makedirs(
    "backend/uploads/claim_images",
    exist_ok=True
)

    saved_paths = []

    file_path = f"backend/uploads/claim_images/{image.filename}"

    with open(file_path, "wb") as f:
        f.write(await image.read())

    saved_paths.append(file_path)
    # Step 2 : Gemini Image Analysis

    analysis = analyze_images(saved_paths)

    # Step 3 : Fraud Detection

    fraud = analyze_fraud(
        analysis)

    # Step 4 : Claim Calculation

    claim = calculate_claim(
        analysis,
        customer_details,
        fraud
    )


    # Step 5 : AI Report

    report = generate_claim_report(

        analysis,

        fraud,

        claim,

        customer_details

    )

    # Step 6 : PDF Generation

    pdf_path = generate_claim_pdf(

        report,

        analysis,

        fraud,

        claim,

        customer_details

    )

    # Step 7 : Store in PostgreSQL

    claim_id, claim_number = save_claim(

    customer_details,

    analysis,

    fraud,

    claim,

    pdf_path,

    saved_paths,

    report

)

    return {

        "success": True,

        "claim_id": claim_id,

        "claim_number": claim_number,

        "analysis": analysis,

        "fraud": fraud,

        "claim": claim,

        "report": report,

        "pdf_path": pdf_path

    }