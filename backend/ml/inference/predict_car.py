import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models" / "car_quote_pipeline.pkl"

car_model = joblib.load(MODEL_PATH)


def predict_car_quote(data: dict):

    df = pd.DataFrame([data])

    prediction = car_model.predict(df)

    return round(float(prediction[0]), 2)