from fastapi import APIRouter
from pydantic import BaseModel

from backend.ml.inference.predict_bike import predict_bike_quote
from backend.ml.inference.predict_car import predict_car_quote
from backend.ml.inference.predict_health import predict_health_quote

from backend.utils.prompt_builder import build_quote_prompt
from backend.utils.gemini_client import gemini_client
from backend.utils.config import GEMINI_MODEL

import traceback

router = APIRouter()


class QuoteRequest(BaseModel):
    insurance_type: str
    details: dict


@router.post("/predict-quote")
def predict_quote(request: QuoteRequest):

    print("\n==============================")
    print("STEP 1 - REQUEST RECEIVED")
    print(request)

    insurance_type = request.insurance_type.strip().lower()
    details = request.details

    print("STEP 2 - Insurance Type :", insurance_type)
    print("STEP 3 - Details :", details)

    # ---------------------------
    # ML Prediction
    # ---------------------------

    if insurance_type == "bike":

        print("STEP 4 - Calling Bike Model")
        premium = predict_bike_quote(details)

    elif insurance_type == "car":

        print("STEP 4 - Calling Car Model")
        premium = predict_car_quote(details)

    elif insurance_type == "health":

        print("STEP 4 - Calling Health Model")
        premium = predict_health_quote(details)

    else:

        return {
            "error": "Invalid insurance type. Choose bike, car or health."
        }

    print("STEP 5 - Predicted Premium :", premium)

    # ---------------------------
    # Gemini Explanation
    # ---------------------------

    try:

        print("STEP 6 - Building Prompt")

        prompt = build_quote_prompt(
            insurance_type=insurance_type,
            details=details,
            predicted_premium=premium
        )

        print("STEP 7 - Calling Gemini")

        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        assistant_response = response.text if response.text else \
    "AI explanation unavailable."

        print("STEP 8 - Gemini Response Received")

    except Exception:
        traceback.print_exc()

        assistant_response = """
<h3>Quote Summary</h3>

<p>
Your insurance premium has been generated successfully.
Our AI explanation is currently unavailable.
Please refer to the premium shown above.
</p>
"""

    print("STEP 9 - Returning Response")

    return {

        "insurance_type": insurance_type,

        "predicted_premium": round(float(premium), 2),

        "assistant_response": assistant_response

    }