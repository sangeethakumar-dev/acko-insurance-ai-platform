import joblib
import pandas as pd
from pathlib import Path

# Load model once
MODEL_PATH = Path(__file__).parent.parent / "models" / "bike_quote_pipeline.pkl"

bike_model = joblib.load(MODEL_PATH)

def predict_bike_quote(data: dict):

    df = pd.DataFrame([data])

    prediction = bike_model.predict(df)

    return round(float(prediction[0]),2)