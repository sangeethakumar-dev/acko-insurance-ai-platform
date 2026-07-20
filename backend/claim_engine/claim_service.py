from backend.claim_engine.image_validator import validate_uploaded_images
from backend.claim_engine.image_analysis import analyze_images
from backend.claim_engine.fraud_checker import analyze_fraud
from backend.claim_engine.claim_calculator import calculate_claim
from backend.claim_engine.report_generator import generate_claim_report

from backend.database.claim_queries import save_claim

import os


async def process_claim(images, customer_details):

    # ==========================================
    # Step 1 : Validate Images
    # ==========================================

    validation = await validate_uploaded_images(images)

    if not validation["valid"]:
        return validation

    print("✅ Step 1 - Validation Done")

    # ==========================================
    # Create Upload Folder
    # ==========================================

    os.makedirs(
        "backend/uploads/claim_images",
        exist_ok=True
    )

    saved_paths = []

    # ==========================================
    # Save Uploaded Images
    # ==========================================

    for image in images:

        file_path = f"backend/uploads/claim_images/{image.filename}"

        with open(file_path, "wb") as f:
            f.write(await image.read())

        saved_paths.append(file_path)

    print("✅ Images Saved Successfully")

    # ==========================================
    # Step 2 : Gemini Image Analysis
    # ==========================================

    analysis = analyze_images(saved_paths)

    print("✅ Step 2 - Image Analysis Done")

    # ==========================================
    # Step 3 : Fraud Detection
    # ==========================================

    fraud = analyze_fraud(analysis)

    print("✅ Step 3 - Fraud Detection Done")

    # ==========================================
    # Step 4 : Claim Calculation
    # ==========================================

    claim = calculate_claim(
        analysis,
        customer_details,
        fraud
    )

    print("✅ Step 4 - Claim Calculation Done")

    # ==========================================
    # Step 5 : Generate AI Report
    # ==========================================

    report = generate_claim_report(
        analysis,
        fraud,
        claim,
        customer_details
    )

    print("✅ Step 5 - Report Generation Done")

    print("\n========== CLAIM RESULT ==========")
    print(claim)
    print("==================================")

    # ==========================================
    # Step 6 : Save into PostgreSQL
    # ==========================================

    claim_id, claim_number = save_claim(
        customer_details,
        analysis,
        fraud,
        claim,
        saved_paths
    )

    print("✅ Step 6 - Saved to PostgreSQL")

    # ==========================================
    # Return Response
    # ==========================================
    print("========== REPORT ==========")
    print(report)
    print("============================")
    
    return {
        "success": True,
        "claim_id": claim_id,
        "claim_number": claim_number,
        "analysis": analysis,
        "fraud": fraud,
        "claim": claim,
        "report": report
    }