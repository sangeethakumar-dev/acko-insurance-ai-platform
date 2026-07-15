from fastapi import APIRouter
from pydantic import BaseModel

from backend.ml.inference.predict_bike import predict_bike_quote
from backend.ml.inference.predict_car import predict_car_quote
from backend.ml.inference.predict_health import predict_health_quote

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
    print("STEP 2 - Insurance Type :", insurance_type)

    details = request.details
    print("STEP 3 - Details :", details)

    if insurance_type == "bike":

        print("STEP 4 - Calling Bike Model")
        premium = predict_bike_quote(details)
        print("STEP 5 - Bike Prediction :", premium)

    elif insurance_type == "car":

        print("STEP 4 - Calling Car Model")
        premium = predict_car_quote(details)
        print("STEP 5 - Car Prediction :", premium)

    elif insurance_type == "health":

        print("STEP 4 - Calling Health Model")

        premium = predict_health_quote(details)

        print("STEP 5 - Health Prediction :", premium)

    else:

        print("STEP X - Invalid Insurance Type")
        print(repr(insurance_type))

        return {
            "error": "Invalid insurance type. Choose bike, car or health."
        }

    print("STEP 6 - Returning Response")

    return {
        "insurance_type": insurance_type,
        "predicted_premium": round(float(premium), 2),
        "assistant_response": "Debug Success"
    }