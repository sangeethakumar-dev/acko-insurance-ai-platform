from backend.claim_engine.image_validator import validate_uploaded_images
from backend.claim_engine.image_analysis import analyze_images
from backend.claim_engine.fraud_checker import analyze_fraud
from backend.claim_engine.claim_calculator import calculate_claim

from backend.database.claim_queries import save_claim

import os
from pathlib import Path
from fastapi import UploadFile

async def process_claim(images, customer_details):

    # Step 1 : Validate Images

    validation = await validate_uploaded_images(images)

    if not validation["valid"]:

        return validation
    
    os.makedirs(
    "backend/uploads/claim_images",
    exist_ok=True
)

    saved_paths = []

    for image in images:

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
    
    print("\n========== CLAIM RESULT ==========")
    print(claim)
    print("==================================")


    # Step 6 : Store in PostgreSQL

    claim_id, claim_number = save_claim(

    customer_details,

    analysis,

    fraud,

    claim,

    saved_paths

)

    return {

        "success": True,

        "claim_id": claim_id,

        "claim_number": claim_number,

        "analysis": analysis,

        "fraud": fraud,

        "claim": claim

    }