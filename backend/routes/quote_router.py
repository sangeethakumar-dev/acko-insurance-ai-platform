from fastapi import APIRouter
from pydantic import BaseModel

from backend.ml.inference.predict_bike import predict_bike_quote
from backend.ml.inference.predict_car import predict_car_quote
from backend.ml.inference.predict_health import predict_health_quote

from backend.utils.prompt_builder import build_quote_prompt
from backend.utils.gemini_client import gemini_client

router = APIRouter()


class QuoteRequest(BaseModel):
    insurance_type: str
    details: dict


@router.post("/predict-quote")
def predict_quote(request: QuoteRequest):

    insurance_type = request.insurance_type.lower()
    details = request.details

    # Route to the correct ML model
    if insurance_type == "bike":
        premium = predict_bike_quote(details)

    elif insurance_type == "car":
        premium = predict_car_quote(details)

    elif insurance_type == "health":
        premium = predict_health_quote(details)

    else:
        return {
            "error": "Invalid insurance type. Choose bike, car or health."
        }

    # Build Gemini prompt
    prompt = build_quote_prompt(
        insurance_type,
        details,
        premium
    )

    # Gemini Response
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "insurance_type": insurance_type,
        "predicted_premium": round(premium, 2),
        "assistant_response": response.text
    }