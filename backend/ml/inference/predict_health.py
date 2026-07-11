import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models" / "health_quote_pipeline.pkl"

health_model = joblib.load(MODEL_PATH)


def predict_health_quote(data: dict):

    df = pd.DataFrame([data])

    prediction = health_model.predict(df)

    return round(float(prediction[0]), 2)