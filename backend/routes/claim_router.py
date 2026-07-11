from typing import List
from fastapi import APIRouter, UploadFile, File, Form

from backend.claim_engine.claim_service import process_claim

router = APIRouter()


@router.post("/claim/analyze")
async def analyze_claim(

    image: UploadFile = File(...),

    customer_name: str = Form(...),

    policy_type: str = Form(...),

    policy_age: str = Form(...),

    annual_premium: float = Form(...),

    previous_claims: str = Form(...),

    ncb: str = Form(...),

    zero_dep: str = Form(...),

    engine_protection: str = Form(...),

    state: str = Form(...),

    age_group: str = Form(...),

    city_tier: str = Form(...)
):

    customer_details = {

        "customer_name": customer_name,

        "policy_type": policy_type,

        "policy_age": policy_age,

        "annual_premium": annual_premium,

        "previous_claims": previous_claims,

        "ncb": ncb,

        "zero_dep": zero_dep,

        "engine_protection": engine_protection,

        "state": state,

        "age_group": age_group,

        "city_tier": city_tier

    }

    return await process_claim(image, customer_details)